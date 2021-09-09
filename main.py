import os

from environs import Env

import vk
from xckd import fetch_random_comic, save_image_from_url


def main():
    image_path = "tmp.png"

    env = Env()
    env.read_env()

    token = env.str("VK_ACCESS_TOKEN")

    comic = fetch_random_comic()
    save_image_from_url(comic["img"], image_path)

    uploaded_comic = vk.upload_image(token, image_path)
    os.remove(image_path)
    album_saved_comic = vk.save_album_comic(token, uploaded_comic)
    vk.publish_comic(token, album_saved_comic, comic["title"])


if __name__ == "__main__":
    main()
