from data_generator import generate_post, fetch_post
import threading
from ApiClient import ApiClient

base_url = 'https://world-bulletin-board.uc.r.appspot.com'
username = 'test1'
password = 'test1234'


def upload_posts():
    api_client = ApiClient(base_url=base_url)
    api_client.login(username, password)

    for i in range(2):
        post = generate_post()
        title = post['title']
        body = post['body']
        lat = post['longitude']
        lon = post['latitude']
        img = post['img']
        post = api_client.create_post(title, body, lat, lon, img)


def test_upload():
    num_threads = 100
    threads = []
    for i in range(num_threads):
        threads.append(threading.Thread(target=upload_posts))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    test_upload()
