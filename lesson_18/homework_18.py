from pathlib import Path
from urllib.parse import urlparse

import requests


BASE_URL = "https://images-api.nasa.gov"
SEARCH_QUERY = "Curiosity rover Mars"
DOWNLOAD_DIR = Path(__file__).resolve().parent
PHOTO_NAMES = ("mars_photo1.jpg", "mars_photo2.jpg")


def search_images(query, page_size=20):
    search_url = f"{BASE_URL}/search"
    search_params = {
        "q": query,
        "media_type": "image",
        "page_size": page_size,
    }

    response = requests.get(search_url, params=search_params, timeout=30)
    response.raise_for_status()
    return response.json()["collection"]["items"]


def get_nasa_ids(search_items):
    nasa_ids = []

    for item in search_items:
        data = item.get("data", [])
        if not data:
            continue

        nasa_id = data[0].get("nasa_id")
        if nasa_id:
            nasa_ids.append(nasa_id)

    return nasa_ids


def get_asset_urls(nasa_id):
    asset_url = f"{BASE_URL}/asset/{nasa_id}"
    response = requests.get(asset_url, timeout=30)
    response.raise_for_status()
    return [
        item["href"]
        for item in response.json()["collection"]["items"]
        if "href" in item
    ]


def is_jpg_url(url):
    file_path = urlparse(url).path.lower()
    return file_path.endswith(".jpg") or file_path.endswith(".jpeg")


def choose_best_jpg(asset_urls):
    jpg_urls = [url for url in asset_urls if is_jpg_url(url)]
    if not jpg_urls:
        return None

    quality_priority = ("~orig", "~large", "~medium", "~small", "~thumb")
    for quality in quality_priority:
        for url in jpg_urls:
            if quality in url.lower():
                return url

    return jpg_urls[0]


def download_image(image_url, output_path):
    response = requests.get(image_url, timeout=60)
    response.raise_for_status()
    output_path.write_bytes(response.content)


def backup_curiosity_photos():
    search_items = search_images(SEARCH_QUERY)
    nasa_ids = get_nasa_ids(search_items)
    downloaded_count = 0

    for nasa_id in nasa_ids:
        asset_urls = get_asset_urls(nasa_id)
        jpg_url = choose_best_jpg(asset_urls)
        if jpg_url is None:
            continue

        output_path = DOWNLOAD_DIR / PHOTO_NAMES[downloaded_count]
        download_image(jpg_url, output_path)
        print(f"Downloaded {output_path.name} from nasa_id={nasa_id}")

        downloaded_count += 1
        if downloaded_count == len(PHOTO_NAMES):
            break

    if downloaded_count < len(PHOTO_NAMES):
        raise RuntimeError("Could not download two JPG images from NASA assets.")


if __name__ == "__main__":
    backup_curiosity_photos()
