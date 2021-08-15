import * as config from '../config';


export async function signup({ username, password, firstName, lastName, emailAddress }) {
    const url = `${config.apiBaseUrl}/signup`;

    const data = new FormData();

    data.append('username', username);
    data.append('password', password);
    data.append('firstName', firstName);
    data.append('lastName', lastName);
    data.append('emailAddress', emailAddress);

    const response = await fetch(url, {
        method: 'POST',
        body: data
    });

    const responseBody = await response.json();

    if (response.status != 200) // if status code is not 200, return undefined
    {
        return undefined
    }
    return responseBody;
}

export async function login({ username, password }) {
    const url = `${config.apiBaseUrl}/login`;
    console.log('Url', url);

    const data = new FormData();

    data.append('username', username);
    data.append('password', password);

    const response = await fetch(url, {
        method: 'POST',
        body: data
    });

    const responseBody = await response.json();
     
    if (response.status != 200) // if status code is not 200, return undefined
    {
        return undefined
    }
    return responseBody;
}

export async function refreshToken() {
    const url = `${config.apiBaseUrl}/refreshToken`;

    const response = await fetch(url, {
        method: 'POST',
        body: data
    });

    const responseBody = await response.json();

    return responseBody;
}
