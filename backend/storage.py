import os
from google.cloud import storage


BUCKET_NAME = os.environ.get('BUCKET_NAME') or "world-bulletin-board.appspot.com"


def create_bucket(bucket_name):
    client = storage.Client()
    bucket = client.create_bucket(bucket_name)
    return bucket


# Save image in Cloud Storage and return its public url
def upload_image(filename, content, content_type):
    client = storage.Client()
    bucket = client.get_bucket(BUCKET_NAME)
    blob = bucket.blob(filename)
    blob.upload_from_string(content, content_type=content_type)
    return blob.public_url
