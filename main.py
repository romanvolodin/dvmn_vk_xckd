from environs import Env

import vk


def main():
    env = Env()
    env.read_env()

    vk_token = env.str("VK_ACCESS_TOKEN")
    upload_url = vk.get_upload_url(vk_token)


if __name__ == "__main__":
    main()
