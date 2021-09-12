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
        "access_token": token,
        "v": vk.API_VERSION,
        "group_id": group_id,
    }
    comic = fetch_random_comic()
    try:
        download_image(comic["img"], image_path)
        uploaded_comic = vk.upload_image(image_path, params)
        album_saved_comic = vk.save_album_comic(uploaded_comic, params)
        vk.publish_comic(album_saved_comic, comic["title"], params)
    finally:
        os.remove(image_path)


if __name__ == "__main__":
    main()
