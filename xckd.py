from random import randint
import requests


def download_image(url, save_path, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(save_path, "wb") as image:
        image.write(response.content)


def fetch_last_comic_id():
    response = requests.get("https://xkcd.com/info.0.json")
    response.raise_for_status()
    return response.json()["num"]


def fetch_random_comic():
    random_id = randint(1, fetch_last_comic_id())
    response = requests.get(f"https://xkcd.com/{random_id}/info.0.json")
    response.raise_for_status()
    return response.json()
