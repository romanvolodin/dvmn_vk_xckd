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

    uploaded_photo = vk.upload_image(token, image_path)
    os.remove(image_path)
    saved_photo = vk.save_album_photo(token, uploaded_photo)
    vk.publish_photo(token, saved_photo)


if __name__ == "__main__":
    main()
