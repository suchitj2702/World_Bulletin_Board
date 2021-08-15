import { StackScreenProps } from '@react-navigation/stack';
import React, { useState, useContext } from 'react';
import { StyleSheet, Text, TouchableOpacity, View, TextInput } from 'react-native';

import { RootStackParamList } from '../types';
import { AuthContext } from '../context/AuthProvider';

export default function LoginScreen({ navigation }:

  StackScreenProps<RootStackParamList, 'Login'>) {

  // Variables that will be used by this tab
  const auth = useContext(AuthContext);
  const [errorMessage, setErrorMessage] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  // attempt to login the user 
  async function handleLogin() {
    try {
      var loginTry = await auth.login({ username, password })

      if (loginTry == 1) // login was successful
      {
        navigation.replace('Root');  // Redirect to root
      }
      else {
        setErrorMessage("Username/Password not found. Try again or create a new account.");
      }

    } catch (e) {
      console.log("error", e);
      setErrorMessage(e.message);
    }

  }

  // redirect to sign up tab
  async function handleSignup() {
    navigation.replace('Signup');
  }

  return (
    <View style={styles.container}>

      <Text>{errorMessage}</Text>
      <Text style={styles.title}>Please Login</Text>
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
      <TouchableOpacity onPress={handleLogin} style={styles.link}>
        <Text style={styles.linkText}>Login</Text>
      </TouchableOpacity>
      <TouchableOpacity onPress={handleSignup} style={styles.link}>
        <Text style={styles.linkText}>Create New Account</Text>
      </TouchableOpacity>
    </View>
  );
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
