from xckd import save_image_from_url, fetch_comic_comment


if __name__ == "__main__":
    save_image_from_url(
        "https://imgs.xkcd.com/comics/python.png", "python.png"
    )
    fetch_comic_comment("https://xkcd.com/353/info.0.json")
