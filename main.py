import os
from environs import Env

import vk
from xckd import fetch_random_comic, save_image_from_url


def main():
    env = Env()
    env.read_env()

    vk_token = env.str("VK_ACCESS_TOKEN")

    image_path = "tmp.png"

    comic = fetch_random_comic()
    save_image_from_url(comic["img"], image_path)

    uploaded_photo = vk.upload_image(vk_token, image_path)
    os.remove(image_path)
    saved_photo = vk.save_album_photo(vk_token, uploaded_photo)
    vk.publish_photo(vk_token, saved_photo)


if __name__ == "__main__":
    main()
