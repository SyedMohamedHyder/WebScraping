import os
import requests

def download_image(url, filename):
    response = requests.get(url)

    filename = os.path.join('rcb_pics', f'{filename}.jpg')

    with open(filename, 'wb') as file:
        file.write(response.content)
