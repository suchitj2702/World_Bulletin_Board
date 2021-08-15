import { StackScreenProps } from '@react-navigation/stack';
import React, { useState, useContext } from 'react';
import { StyleSheet, Text, TouchableOpacity, View, TextInput } from 'react-native';

import { RootStackParamList } from '../types';
import { AuthContext } from '../context/AuthProvider';

export default function SignupScreen({ navigation }:

  StackScreenProps<RootStackParamList, 'Signup'>) {
  // Variables that will be used by this tab
  const auth = useContext(AuthContext);
  const [errorMessage, setErrorMessage] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [firstName, setfirstName] = useState("");
  const [lastName, setlastName] = useState("");
  const [emailAddress, setemailAddr] = useState("");

  // attmepts to create a new user in the user table
  async function handleSignup() {
    if (username && password && firstName && lastName && emailAddress) // check that all required fields are filled out
    {
      try {
        var signupTry = await auth.signup({ username, password, firstName, lastName, emailAddress })

        if (signupTry == 1) {
          navigation.replace('Root');  // Redirect to root
        }
        else {
          setErrorMessage("Error creating user. Try again.");
        }

      } catch (e) {
        console.log("error", e);
        setErrorMessage(e.message);
      }
    } else {
      setErrorMessage("Make sure all fields are filled out")
    }

  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Create New Account</Text>
      <TextInput
        style={styles.input}
        placeholder="Username"
        onChangeText={text => setUsername(text)}
      />
      <TextInput
        style={styles.input}
        placeholder="Password"
        onChangeText={text => setPassword(text)}
      />
      <TextInput
        style={styles.input}
        placeholder="First Name"
        onChangeText={text => setfirstName(text)}
      />
      <TextInput
        style={styles.input}
        placeholder="Last Name"
        onChangeText={text => setlastName(text)}
      />
      <TextInput
        style={styles.input}
        placeholder="Email Address"
        onChangeText={text => setemailAddr(text)}
      />
      <TouchableOpacity onPress={handleSignup} style={styles.link}>
        <Text style={styles.linkText}>Create Account</Text>
      </TouchableOpacity>
      <TouchableOpacity onPress={handleLogin} style={styles.link}>
        <Text style={styles.linkText}>Login to existing account</Text>
      </TouchableOpacity>
      <Text>{errorMessage}</Text>
    </View>
  );
  function handleLogin() {
    navigation.replace('Login');
  }
}

// styles used by components 
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 20,
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  link: {
    marginTop: 15,
    paddingVertical: 15,
  },
  linkText: {
    fontSize: 14,
    color: '#2e78b7',
  },
  input: {
    height: 40,
    margin: 15,
    borderWidth: 1,
    width: 200,
  },
});
