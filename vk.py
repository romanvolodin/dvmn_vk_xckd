import requests


API_BASE_URL = "https://api.vk.com/method"
API_VERSION = 5.131


def get_upload_url(params):
    response = requests.get(
        f"{API_BASE_URL}/photos.getWallUploadServer", params=params
    )
    response.raise_for_status()
    return response.json()["response"]["upload_url"]


def upload_image(image_path, params):
    with open(image_path, "rb") as image:
        response = requests.post(
            get_upload_url(params), files={"photo": image}
        )
    response.raise_for_status()
    return response.json()


def save_album_comic(uploaded_comic, params):
    params.update({
        "photo": uploaded_comic["photo"],
        "server": uploaded_comic["server"],
        "hash": uploaded_comic["hash"],
    })
    response = requests.post(
        f"{API_BASE_URL}/photos.saveWallPhoto", params=params
    )
    response.raise_for_status()
    return response.json()["response"][0]


def publish_comic(saved_comic, title, params):
    attachment_template = "photo{owner_id}_{media_id}"
    params.update({
        "owner_id": params["group_id"] * -1,
        "from_group": 1,
        "message": title,
        "attachments": attachment_template.format(
            owner_id=saved_comic["owner_id"],
            media_id=saved_comic["id"],
        ),
    })
    response = requests.post(f"{API_BASE_URL}/wall.post", params=params)
    response.raise_for_status()
    return response.json()
