from data_generator import generate_post, fetch_post
import threading
from ApiClient import ApiClient

base_url = 'https://world-bulletin-board.uc.r.appspot.com'
username = 'test1'
password = 'test1234'


def retrieve_post():
    api_client = ApiClient(base_url=base_url)
    api_client.login(username, password)

    latitude, longitude, rand_radius, rand_tags = fetch_post()
    posts = api_client.get_post(latitude, longitude, rand_radius * 2000, rand_tags)


def test_get_posts():
    num_threads = 500
    threads = []
    for i in range(num_threads):
        threads.append(threading.Thread(target=retrieve_post))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    test_get_posts()
