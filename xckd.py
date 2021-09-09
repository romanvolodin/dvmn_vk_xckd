import requests


def save_image_from_url(url, save_path, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(save_path, "wb") as image:
        image.write(response.content)


def fetch_comic_comment(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["alt"]
