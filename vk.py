import requests


API_BASE_URL = "https://api.vk.com/method"
API_VERSION = 5.131
VK_GROUP_ID = 207032382


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


def save_album_comic(token, uploaded_comic):
    response = requests.post(
        f"{API_BASE_URL}/photos.saveWallPhoto",
        params={
            "access_token": token,
            "v": API_VERSION,
            "group_id": VK_GROUP_ID,
            "photo": uploaded_comic["photo"],
            "server": uploaded_comic["server"],
            "hash": uploaded_comic["hash"],
        }
    )
    response.raise_for_status()
    return response.json()["response"][0]


def publish_comic(token, saved_comic, title):
    attachment_template = "photo{owner_id}_{media_id}"
    attachment = attachment_template.format(
        owner_id=saved_comic["owner_id"],
        media_id=saved_comic["id"],
    )
    response = requests.post(
        f"{API_BASE_URL}/wall.post",
        params={
            "access_token": token,
            "v": API_VERSION,
            "owner_id": VK_GROUP_ID * -1,  # group_id must be negative int
            "from_group": 1,
            "attachments": attachment,
            "message": title,
        }
    )
    response.raise_for_status()
    return response.json()
