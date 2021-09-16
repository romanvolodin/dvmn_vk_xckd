import os

from environs import Env

import vk
from xckd import fetch_random_comic, download_image


def main():
    image_path = "tmp.png"

    env = Env()
    env.read_env()

    token = env.str("VK_ACCESS_TOKEN")
    group_id = env.int("VK_GROUP_ID")

    params = {
        "api_token": token,
        "api_version": vk.API_VERSION,
        "group_id": group_id,
    }
    comic = fetch_random_comic()
    download_image(comic["img"], image_path)
    try:
        upload_url = vk.get_upload_url(**params)
        uploaded_comic = vk.upload_image(upload_url, image_path)
        saved_comic = vk.save_album_comic(
            uploaded_comic["photo"],
            uploaded_comic["server"],
            uploaded_comic["hash"],
            **params,
        )
        vk.publish_comic(
            saved_comic["owner_id"],
            saved_comic["id"],
            comic["title"],
            **params,
        )
    finally:
        os.remove(image_path)


if __name__ == "__main__":
    main()
