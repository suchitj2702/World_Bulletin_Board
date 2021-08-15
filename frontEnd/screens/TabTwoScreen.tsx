import React, { useState, useEffect, useContext } from 'react';
import { StyleSheet, Button, Image, TextInput, Platform, View, Text } from 'react-native';
import * as ImagePicker from 'expo-image-picker';
import * as Location from 'expo-location';
import { AuthContext } from '../context/AuthProvider';
import * as config from '../config';

export default function TabTwoScreen() {
  // Variables that will be used by this tab
  const [getStatus, setStatus] = useState("Please Wait...");
  const [getTitle, setTitle] = useState(null);
  const [getBody, setBody] = useState(null);
  const [image, setImage] = useState(null);
  const [getLocation, setLocation] = useState(null);
  const [errorMsg, setErrorMsg] = useState(String);
  const [getLat, setLat] = useState(null);
  const [getLong, setLong] = useState(null);
  const auth = useContext(AuthContext);


  useEffect(() => {
    if (getLocation == null) {
      (async () => {
        let { status } = await Location.requestPermissionsAsync();  // request location permission
        if (status !== 'granted') {
          setErrorMsg('Permission to access location was denied');
          return;
        }

        let location = await Location.getCurrentPositionAsync({});  // get user's location
        setLocation(location);
      })();
    }
  }, [])

  if (errorMsg) { // location not recieved
    setStatus(errorMsg);
  } else if (getLocation && !getLat) {

    var lat = JSON.stringify(getLocation['coords']['latitude']);
    setLat(lat)
  } else if (getLocation && !getLong) {

    var lon = JSON.stringify(getLocation['coords']['longitude']);
    setLong(lon)
  }
  else if (getLat && getLong && getStatus == "Please Wait...") { // location, lat and long set successfully
    //console.log(getLat, getLong)
    setStatus(null)
  }

  useEffect(() => {
    (async () => {
      if (Platform.OS !== 'web') {  // permission not needed on web
        const { status } = await ImagePicker.requestMediaLibraryPermissionsAsync(); // get permission to select image
        if (status !== 'granted') {
          alert('Sorry, we need camera roll permissions to make this work!');
        }
      }
    })();
  }, []);

  // display image picker
  const pickImage = async () => {
    let result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.All,
      allowsEditing: true,
      aspect: [3, 3],
      quality: 0.25,
      base64: true,
    });

    //console.log(result);

    if (!result.cancelled) {
      if (Platform.OS == 'web') {
        setImage(result.uri);
      }
      else {
        setImage("data:image/jpeg;base64," + result.base64)
      }
    }
  };

  if (getStatus == "Please Wait...") { // location has not been determined yet
    return (
      <View style={styles.container}>
        <Text style={styles.title}>{getStatus}</Text>
      </View>
    )
  } else {
    return (
      <View style={styles.container}>
        <Text style={styles.title}>{getStatus}</Text>
        {image && <Image source={{ uri: image }} style={{ width: 200, height: 200 }} />}

        <TextInput
          style={styles.input}
          placeholder="Title"
          onChangeText={text => setTitle(text)}
        />
        <TextInput
          returnKeyType={'done'}
          blurOnSubmit={true}
          style={styles.description}
          multiline={true}
          placeholder="Describe your pin here"
          onChangeText={text => setBody(text)}
        />
        <View style={styles.space}></View>
        <Button title="Add Image to Pin" onPress={pickImage} />
        <View style={styles.space}>
        </View><View style={styles.space}></View>
        <Button
          onPress={() => {
            // append needed fields to HTTP request and attempt to upload the post to database
            var data = new FormData();
            data.append("title", getTitle);
            data.append("body", getBody);
            data.append("img", image);
            data.append("lat", getLat);
            data.append("long", getLong);

            var xhr = new XMLHttpRequest();
            xhr.withCredentials = true;

            // listen for response 
            xhr.addEventListener("readystatechange", function () {
              if (this.readyState === 4) {
                console.log(this.responseText);
                if (this.status == 200)  // upload was successful
                {
                  setStatus(getTitle + " uploaded Successfully!");
                } else {
                  setStatus('Error ' + this.status.toString())
                }
              }
            });

            xhr.open("POST", `${config.apiBaseUrl}/upload`);    // update url when decided
            // only authorized users may post
            xhr.setRequestHeader('Authorization', `Bearer ${auth.token}`);

            if (getTitle && getBody && image && getLat && getLong) {  // check all required fields present
              xhr.send(data);
              setStatus("Uploading...")
            } else {
              setStatus("Please ensure all fields are filled out")
            }
          }}
          title={"Upload Pin"}
        />
      </View>
    );
  }
}

// styles used by components 
const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    padding: 10,
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
    padding: 10,
  },
  separator: {
    marginVertical: 30,
    height: 1,
    width: '80%',
  },
  input: {
    height: 40,
    margin: 15,
    borderWidth: 1,
    width: 200,
  },
  description: {
    height: 120,
    margin: 15,
    borderWidth: 1,
    width: 300,
  },
  space: {
    width: 20,
    height: 15
  },

});
