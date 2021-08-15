import React, { useState } from 'react';
import * as auth from '../utils/auth';


export const AuthContext = React.createContext({
    signup: async ({ username, password, firstName, lastName, emailAddress }) => { },
    login: async ({ username, password }) => { },
    token: '',
    user: null
});


export default function AuthProvider({ children }) {
    const [token, setToken] = useState('');
    const [user, setUser] = useState(null);

    async function signup({ username, password, firstName, lastName, emailAddress }) {
        const responseBody = await auth.signup({ username, password, firstName, lastName, emailAddress });

        if (responseBody != undefined) {
            setToken(responseBody.token);
            setUser(responseBody.user);
            return 1 // user signed in successfully

        }
        else {
            console.log("Signin Error")
            return 0 // user not signed in
        }
    }

    async function login({ username, password }) {
        const responseBody = await auth.login({ username, password })

        if (responseBody != undefined) {
            setToken(responseBody.token);
            setUser(responseBody.user);
            console.log('Token:', responseBody.token);
            console.log('User:', responseBody.user);
            return 1 // user signed in successfully

        }
        else {
            console.log("Login Error")
            return 0 // user not signed in
        }
    }

    return (
        <AuthContext.Provider
            value={{
                signup,
                login,
                token,
                user
            }}
        >
            {children}
        </AuthContext.Provider>
    )
}
