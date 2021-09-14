import requests


API_BASE_URL = "https://api.vk.com/method"
API_VERSION = 5.131


def get_upload_url(api_token, api_version, group_id):
    params = {
        "access_token": api_token,
        "v": api_version,
        "group_id": group_id,
    }
    response = requests.get(
        f"{API_BASE_URL}/photos.getWallUploadServer", params=params
    )
    check_error(response)
    return response.json()["response"]["upload_url"]


def upload_image(url, image_path):
    with open(image_path, "rb") as image:
        response = requests.post(url, files={"photo": image})
    check_error(response)
    return response.json()


def save_album_comic(uploaded_comic, api_token, api_version, group_id):
    params = {
        "access_token": api_token,
        "v": api_version,
        "group_id": group_id,
        "photo": uploaded_comic["photo"],
        "server": uploaded_comic["server"],
        "hash": uploaded_comic["hash"],
    }
    response = requests.post(
        f"{API_BASE_URL}/photos.saveWallPhoto", params=params
    )
    check_error(response)
    return response.json()["response"][0]


def publish_comic(saved_comic, title, api_token, api_version, group_id):
    attachment_template = "photo{owner_id}_{media_id}"
    params = {
        "access_token": api_token,
        "v": api_version,
        "owner_id": group_id * -1,
        "from_group": 1,
        "message": title,
        "attachments": attachment_template.format(
            owner_id=saved_comic["owner_id"],
            media_id=saved_comic["id"],
        ),
    }
    response = requests.post(f"{API_BASE_URL}/wall.post", params=params)
    check_error(response)
    return response.json()


def check_error(response):
    deserialized_response = response.json()
    if "error" in deserialized_response:
        raise requests.exceptions.HTTPError(deserialized_response["error"])
    response.raise_for_status()
