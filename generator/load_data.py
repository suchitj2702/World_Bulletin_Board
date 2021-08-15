from data_generator import generate_post
import threading
from ApiClient import ApiClient

base_url = 'https://world-bulletin-board.uc.r.appspot.com'
username = 'test2'
password = 'test1234'


def load_data():
    api_client = ApiClient(base_url=base_url)
    api_client.login(username, password)

    for i in range(1000):
        post = generate_post(single_threaded=True)
        title = post['title']
        body = post['body']
        lat = post['longitude']
        lon = post['latitude']
        img = post['img']
        post = api_client.create_post(title, body, lat, lon, img)
        #print('Created post:', post)


if __name__ == '__main__':
    load_data()
