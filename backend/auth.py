import os
from flask import Flask, render_template, request, make_response
import datetime
import jwt
import bcrypt


ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET') or 'abc'
REFRESH_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET') or 'def'

# Functions for JWT generation

# Expires in 15 min
def get_access_token(user_id):
    payload = {
        'userId': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }
    token = jwt.encode(payload, ACCESS_TOKEN_SECRET, algorithm='HS256')
    return token


# Expires in 30 days
def get_refresh_token(user_id):
    payload = {
        'userId': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30)
    }
    token = jwt.encode(payload, REFRESH_TOKEN_SECRET, algorithm='HS256')
    return token


# Verify access token and extract user ID from payload
def get_user_id_from_auth():
    # Check Authorization header
    authorization = request.headers.get('Authorization')
    auth_split = authorization.split(' ')
    if len(auth_split) != 2 or auth_split[0] != 'Bearer':
        return None
    token = auth_split[1]
    payload = None
    try:
        payload = jwt.decode(token, ACCESS_TOKEN_SECRET, algorithms=['HS256'])
    except:
        return None
    return payload.get('userId')


# Verify refresh token and extract user ID from payload
def get_user_id_from_refresh_token():
    token = request.cookies.get('refreshToken')
    if token is None:
        return None
    payload = None
    try:
        payload = jwt.decode(token, REFRESH_TOKEN_SECRET, algorithms=['HS256'])
    except:
        return None
    return payload.get('userId')


# Hash user password using bcrypt
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(bytes(password, encoding='utf-8'), salt)
    return hashed_password.decode('utf-8')


# Verify a plaintext password against a password hash
def verify_password(password, hashed_password):
    return bcrypt.checkpw(bytes(password, encoding='utf-8'), bytes(hashed_password, encoding='utf-8'))
