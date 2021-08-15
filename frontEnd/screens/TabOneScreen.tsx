import React, { useState, useEffect, useContext, useRef } from 'react';
import { Platform, Image, Button, StyleSheet, FlatList } from 'react-native';
import * as Location from 'expo-location';
import { Text, View } from '../components/Themed';
import { AuthContext } from '../context/AuthProvider';
import * as config from '../config';
import Constants from 'expo-constants';
import * as Notifications from 'expo-notifications';
import AsyncStorage from '@react-native-async-storage/async-storage';
console.disableYellowBox = true;

// Handles notifications when they come in
Notifications.setNotificationHandler({
  handleNotification: async () => ({
    shouldShowAlert: true,
    shouldPlaySound: false,
    shouldSetBadge: false,
  }),
});

export default function TabOneScreen() {

  // Variables that will be used by this tab
  const [location, setLocation] = useState(null);
  const [errorMsg, setErrorMsg] = useState(String);
  const [getText, setText] = useState("Loading...");
  const [getPosts, setPosts] = useState(JSON.parse("{\"posts\": [{\"title\" : \"\"}]}"));
  const [notificationSent, setNotificationSent] = useState(false);
  const [tags, setTags] = useState("");

  // Gets user's preferences from persistant storage
  const getData = async () => {
    try {
      var value = await AsyncStorage.getItem('@storage_Key')
      if (value) {
        var interests = JSON.parse(value)
        setTags(interests)
      }
    } catch (e) {
      console.log(e)
    }
  }


  useEffect(() => {
    if (!location)   // check if location has been determined or not already
    {
      // gets the location of the device
      (async () => {
        let { status } = await Location.requestPermissionsAsync();
        if (status !== 'granted') {
          setErrorMsg('Permission to access location was denied');
          return;
        }

        let location = await Location.getCurrentPositionAsync({});

        //console.log(location) 
        setLocation(location);
      })();
    }

  }, [])
  if (errorMsg) {   // there was an error determining the location 
    setText(errorMsg);
  } else if (location) {    // location determined successfully
    var lat = JSON.stringify(location['coords']['latitude']);
    var long = JSON.stringify(location['coords']['longitude']);

    // create HTTP Request to get posts for the user
    var xhr = new XMLHttpRequest();
    xhr.withCredentials = false;

    // listens for response from the request 
    xhr.addEventListener("readystatechange", function () {
      if (this.readyState === 4) {
        let results = this.responseText;
        setText("") // Signifies that a response has been received
        try {
          setPosts(JSON.parse(results))
          console.log(JSON.parse(results))
        }
        catch (e) {
          console.log(e)
        }
      }
    })

    // encode the url with necessary parameters and send request
    const url = `${config.apiBaseUrl}/posts?lat=${encodeURIComponent(lat)}&long=${encodeURIComponent(long)}&radius=20000&tags=${encodeURIComponent(tags)}`
    console.log(url)
    xhr.open("GET", url);

    if (getText != "")   // will only send the http request once. This prevents the app from re-rendering endlessly 
    {
      xhr.send();
    }
  }


  // This is called when the 'refresh' button is pressed. It will resend the HTTP request to get relevent posts from the database
  async function updateList() {
    //console.log('updating')
    var xhr = new XMLHttpRequest();
    xhr.withCredentials = false;


    // listens for response from the request 
    xhr.addEventListener("readystatechange", function () {
      if (this.readyState === 4) {
        let results = this.responseText;
        setText("")
        try {
          setPosts(JSON.parse(results))
          console.log(JSON.parse(results))
        }
        catch (e) {
          console.log(e)
        }
      }
    })
    // retrieve user's preferences from persistant storage
    await getData()

    // encode the url with necessary parameters and send request
    const url = `${config.apiBaseUrl}/posts?lat=${encodeURIComponent(lat)}&long=${encodeURIComponent(long)}&radius=2000&tags=${encodeURIComponent(tags)}`
    console.log(url)
    setText('Refreshing...')
    xhr.open("GET", url);
    xhr.send();
  }

  if (Platform.OS != 'web' && !notificationSent) // will schedule a notification to be sent to the user
  {
    schedulePushNotification();
    setNotificationSent(true) // only schedule on notification 
  }

  return (
    <View style={styles.container}>
      <Text>{getText}</Text>
      <Button title='Refresh' onPress={updateList}></Button>
      <FlatList
        data={getPosts['posts']}
        renderItem={({ item }) =>
          <View style={styles.container}>

            <Text adjustsFontSizeToFit={true} style={styles.title} >{item["title"]}</Text>
            <Image source={{ uri: item['imgUrl'] }} resizeMethod='resize' style={{ width: 200, height: 200, resizeMode: 'center' }} />
            <Text style={styles.item}>{item['body']}</Text>
          </View>}
      />
    </View>
  )
}

// schedule the push notification 
async function schedulePushNotification() {
  await Notifications.scheduleNotificationAsync({
    content: {
      title: "Events near you!!!",
      body: "Come check out events near you!",
      data: { data: 'goes here' },
    },
    trigger: { seconds: 60 }
  });
}

// styles used by components 
const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    paddingTop: 22
  },
  title: {
    fontSize: 22,
    fontWeight: 'bold',
  },
  separator: {
    marginVertical: 30,
    height: 1,
    width: '80%',
  },
  item: {
    padding: 10,
    fontSize: 14,
    textAlign: 'center'
  },
});
