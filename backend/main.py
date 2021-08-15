from flask import Flask, render_template, request, make_response
from flask_cors import CORS
import storage
import db
import auth
import base64

app = Flask(__name__)
CORS(app, supports_credentials =True)


# Test route for quickly checking that backend is up and running
@app.route('/')
def index():
    message = 'Hello there'
    return message


@app.route('/signup', methods=['POST'])
def signup():
    # Parse request body for create user params
    username = request.form.get('username')
    password = request.form.get('password')
    first_name = request.form.get('firstName')
    last_name = request.form.get('lastName')
    email_address = request.form.get('emailAddress')

    # Hash the password
    hashed_password = auth.hash_password(password)

    # Insert new user into the database
    user = db.create_user(username, hashed_password, email_address, first_name, last_name)

    # Create JWT access and refresh tokens for user
    access_token = auth.get_access_token(user['id'])
    refresh_token = auth.get_refresh_token(user['id'])

    # Create response object
    response_payload = {
        'token': access_token,
        'user': user
    }
    response = make_response(response_payload)

    # Store refresh token in HTTP only cookie
    response.set_cookie('refreshToken', refresh_token, httponly=True)

    return response


@app.route('/login', methods=['POST'])
def login():
    # Get username and password from request body
    username = request.form.get('username')
    password = request.form.get('password')

    if username == '' or password == '':
        return { 'message': 'Missing required parameters.' }, 400

    # Retreive user from database
    result = db.get_user_by_username(username)

    # Check if password matches
    hashed_password = result['hashed_password']
    matches = auth.verify_password(password, hashed_password)

    if not matches:
        return { 'message': 'Invalid credentials.' }, 401

    # Create user object (excluding hashed_password)
    user = {
        'id': result['id'],
        'username': result['username'],
        'firstName': result['firstName'],
        'lastName': result['lastName'],
        'emailAddress': result['emailAddress'],
        'createdAt': result['createdAt']
    }

    # Create JWT access and refresh tokens for user
    access_token = auth.get_access_token(user['id'])
    refresh_token = auth.get_refresh_token(user['id'])

    # Create response object
    response_payload = {
        'token': access_token,
        'user': user
    }
    response = make_response(response_payload)

    # Store refresh token in HTTP only cookie
    response.set_cookie('refreshToken', refresh_token, httponly=True)

    return response


@app.route('/refresh_token', methods=['POST'])
def refresh_token():
    user_id = auth.get_user_id_from_refresh_token()
    if user_id is None:
        return { "message": "Invalid refresh token" }, 401

    # Retreive user from database
    user = db.get_user_by_id(user_id)

    if user is None:
        return { "message": "User not found" }, 404

    # Create new access token
    access_token = auth.get_access_token(user['id'])

    return {
        'token': access_token,
        'user': user
    }



@app.route('/posts', methods=['GET'])     
def posts():
    curr_latitude = request.args.get('lat')
    curr_longitude = request.args.get('long')
    radius_km = request.args.get('radius', '10')
    tags_str = request.args.get('tags', '')
    curr_tags = tags_str.split(',') if tags_str != '' else []

    posts = db.get_posts(curr_latitude, curr_longitude, radius_km, curr_tags)

    return {
        'posts': posts
    }


@app.route('/upload', methods=['POST'])
def upload():
    user_id = auth.get_user_id_from_auth()
    if user_id is None:
        return { "message": "Unauthorized" }, 401

    # Parse params
    img = request.form.get('img')  # Base64 encoded image
    title = request.form.get('title')
    body = request.form.get('body')
    latitude = request.form.get('lat')
    longitude = request.form.get('long')

    if title is None or body is None or latitude is None or longitude is None:
        return { "message": "missing required parameters" }, 400

    post = db.create_post(user_id, title, body, latitude, longitude)

    # Save file in storage, if the user upload a file
    if img is not None:
        # Convert image from base 64 to bytes array
        img_bytes = base64.b64decode(img.split(',')[-1])
        post_id = post['id']

        content_type = img.split(';')[0].split(':')[1]
        ext = content_type.split('/')[1]  # File extension (e.g. PNG)

        img_url = storage.upload_image(f'{post_id}.{ext}', img_bytes, content_type)
        db.set_img_url(post_id, img_url)
        post['img_url'] = img_url

    return post

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)
