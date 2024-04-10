import json
import requests
import os
import random
import string
import os
from PIL import Image
from io import BytesIO


def read_json(root_path):
    print('=====================', root_path)
    print('=====================', os.path.join(root_path, 'config.json'))
    with open(os.path.join(root_path, 'config.json')) as json_file:
        data = json.load(json_file)
        return data


def save_image_from_url(url, filename):
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        # Send a GET request to the URL to download the image
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any errors

        # Open the downloaded image using PIL
        image = Image.open(BytesIO(response.content))

        # Save the image as JPG
        image.save(filename, format='JPEG')

    except Exception as e:
        print(f"Error saving image: {e}")


def generate_random_string(length=12):
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
