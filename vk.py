import requests


API_BASE_URL = "https://api.vk.com/method"
API_VERSION = 5.131
VK_GROUP_ID = 207032382


def fetch_groups(token):
    response = requests.get(
        f"{API_BASE_URL}/groups.get",
        params={
            "access_token": token,
            "v": API_VERSION,
            "extended": True,
            "count": 10,
        }
    )
    response.raise_for_status()
    return response.json()


def get_upload_url(token):
    response = requests.get(
        f"{API_BASE_URL}/photos.getWallUploadServer",
        params={
            "access_token": token,
            "v": API_VERSION,
            "group_id": VK_GROUP_ID,
        }
    )
    response.raise_for_status()
    return response.json()["response"]["upload_url"]


def upload_image(token, image_path):
    with open(image_path, "rb") as image:
        response = requests.post(
            get_upload_url(token),
            files={"photo": image},
        )
    response.raise_for_status()
    return response.json()


def save_album_photo(token, photo):
    response = requests.post(
        f"{API_BASE_URL}/photos.saveWallPhoto",
        params={
            "access_token": token,
            "v": API_VERSION,
            "group_id": VK_GROUP_ID,
            "photo": photo["photo"],
            "server": photo["server"],
            "hash": photo["hash"],
        }
    )
    response.raise_for_status()
    return response.json()
