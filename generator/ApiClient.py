import requests

class ApiClient:
    def __init__(self, base_url='http://localhost:3000'):
        self.session = requests.Session()
        self.base_url = base_url

    def login(self, username, password):
        url = f'{self.base_url}/login'
        data = {
            'username': username,
            'password': password
        }
        response = self.session.post(url, data=data)
        response_json = response.json()
        token = response_json.get('token')
        user = response_json.get('user')
        print(f'Logged in as {user}')
        self.session.headers.update({'Authorization': f'Bearer {token}'})  # Set auth token

    def create_post(self, title, body, lat, lon, img):
        url = f'{self.base_url}/upload'
        data = {
            'title': title,
            'body': body,
            'lat': lat,
            'long': lon,
            'img': img
        }
        response = self.session.post(url, data=data)
        post = response.json()
        post_id = post.get('id')
        print(f'Created post with id = {post_id}')
        return post

    def get_post(self, lat, lon, radius_km, tags):
        url = f'{self.base_url}/posts'
        params = {
            'lat': lat,
            'long': lon,
            'radius': radius_km,
            'tags': ",".join(tags)
        }
        response = self.session.get(url, params=params)
        response_json = response.json()
        posts = response_json.get('posts')
        if posts is not None:
            print(f'Retreived {len(posts)} posts')
        return posts
