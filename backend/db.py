import os
import psycopg2
from Cloud_Natural_Language_categorize import tag_text
import traceback


DB_NAME = os.environ.get('DB_NAME') or 'cse546project2'
DB_USER = os.environ.get('DB_USER') or 'postgres'
DB_PASSWORD = os.environ.get('DB_PASSWORD') or 'postgres'
DB_HOST = os.environ.get('DB_HOST') or 'localhost'
DB_PORT = os.environ.get('DB_PORT') or '5432'


def get_db_connection():
    return psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port= DB_PORT)


# Create user and return user object
def create_user(username, hashed_password, email_address, first_name=None, last_name=None):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO users (
            username,
            hashed_password,
            first_name,
            last_name,
            email_address
        )
            VALUES (%s, %s, %s, %s, %s)
            RETURNING
                id,
                username,
                first_name,
                last_name,
                email_address,
                created_at;
    """, (username, hashed_password, first_name, last_name, email_address))

    result = cur.fetchone()
    conn.commit()

    # Create user object
    user = {
        'id': result[0],
        'username': result[1],
        'firstName': result[2],
        'lastName': result[3],
        'emailAddress': result[4],
        'createdAt': result[5]
    }

    conn.close()

    return user


# Get user by username
def get_user_by_username(username):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            id,
            username,
            hashed_password,
            first_name,
            last_name,
            email_address,
            created_at
        FROM users
        WHERE username = %s
    """, (username,))

    result = cur.fetchone()

    # Create user object
    user = {
        'id': result[0],
        'username': result[1],
        'hashed_password': result[2],
        'firstName': result[3],
        'lastName': result[4],
        'emailAddress': result[5],
        'createdAt': result[6],
    }

    conn.commit()
    conn.close()

    return user


# Get user by user id
def get_user_by_id(user_id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            id,
            username,
            first_name,
            last_name,
            email_address,
            created_at
        FROM users
        WHERE id = %s
    """, (user_id,))

    result = cur.fetchone()

    # Create user object
    user = {
        'id': result[0],
        'username': result[1],
        'firstName': result[2],
        'lastName': result[3],
        'emailAddress': result[4],
        'createdAt': result[5]
    }

    conn.commit()
    conn.close()

    return user


# Create a new post
def create_post(user_id, title, body, latitude, longitude):
    try:
        tags = tag_text(body)  # Generate tags
    except:
        traceback.print_exc()
        tags = []

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO posts (
            author_id,
            title,
            body,
            latitude,
            longitude,
            tags
        )
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING
                id,
                author_id,
                title,
                body,
                longitude,
                latitude,
                tags;
    """, (user_id, title, body, latitude, longitude, tags))

    result = cur.fetchone()

    post = {
        'id': result[0],
        'authorId': result[1],
        'title': result[2],
        'body': result[3],
        'lat': result[4],
        'long': result[5],
        'tags' : result[6]
    }

    conn.commit()
    conn.close()

    return post


# Set url of img
def set_img_url(post_id, img_url):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE posts
        SET img_url = %s
        WHERE id = %s
    """, (img_url, post_id))

    conn.commit()
    conn.close()


# Should return posts that are close to the user
def get_posts(curr_latitude, curr_longitude, radius_km, curr_tags):
    conn = get_db_connection()
    cur = conn.cursor()

    if (len(curr_tags) == 0):
        cur.execute("""
            SELECT id, author_id, title, body, img_url, latitude, longitude, tags
            FROM posts
            WHERE
                ST_DWithin(ST_MakePoint(longitude, latitude)::geography, ST_MakePoint(%s, %s)::geography, %s * 1000)
        """, (curr_longitude, curr_latitude, radius_km))
    else:
        cur.execute("""
            SELECT id, author_id, title, body, img_url, latitude, longitude, tags
            FROM posts
            WHERE
                ST_DWithin(ST_MakePoint(longitude, latitude)::geography, ST_MakePoint(%s, %s)::geography, %s * 1000) AND
                tags && %s::TEXT[]
        """, (curr_longitude, curr_latitude, radius_km, curr_tags))

    results = cur.fetchall()

    posts = [{
        'id': result[0],
        'authorId': result[1],
        'title': result[2],
        'body': result[3],
        'imgUrl': result[4],
        'lat': result[5],
        'long': result[6],
        'tags' : result[7]
    } for result in results]

    conn.commit()
    conn.close()

    return posts
