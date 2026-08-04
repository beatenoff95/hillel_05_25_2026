import base64
from pathlib import Path
from urllib.parse import quote, urlparse

import requests


BASE_URL = "http://127.0.0.1:8080"
CURRENT_DIR = Path(__file__).resolve().parent
IMAGE_PATH = CURRENT_DIR / "test_image.jpg"


TEST_IMAGE_BASE64 = (
    "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAP//////////////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////2wBDAf//////////////////////////////////////////////////////////////////////////////////////"
    "////////////////////////////////////////////wAARCAABAAEDASIAAhEBAxEB/8QAFQABAQAAAAAAAAAAAAAAAAAAAAX/xAAUEAEAAAAAAAAAAAAAAAAAAAAA/"
    "9oADAMBAAIQAxAAAAH/xAAUEAEAAAAAAAAAAAAAAAAAAAAA/9oACAEBAAEFAqf/xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oACAEDAQE/ASP/xAAUEQEAAAAAAAAA"
    "AAAAAAAAAAAA/9oACAECAQE/ASP/xAAUEAEAAAAAAAAAAAAAAAAAAAAA/9oACAEBAAY/Ar//xAAUEAEAAAAAAAAAAAAAAAAAAAAA/9oACAEBAAE/IV//2gAMAwEA"
    "AgADAAAAEP/EABQRAQAAAAAAAAAAAAAAAAAAABD/2gAIAQMBAT8QH//EABQRAQAAAAAAAAAAAAAAAAAAABD/2gAIAQIBAT8QH//EABQQAQAAAAAAAAAAAAAAAAAA"
    "ABD/2gAIAQEAAT8QH//Z"
)


def create_test_image():
    IMAGE_PATH.write_bytes(base64.b64decode(TEST_IMAGE_BASE64))
    return IMAGE_PATH


def upload_image(image_path):
    upload_url = f"{BASE_URL}/upload"

    with image_path.open("rb") as image_file:
        files = {"image": (image_path.name, image_file, "image/jpeg")}
        response = requests.post(upload_url, files=files, timeout=30)

    response.raise_for_status()
    return response.json()["image_url"]


def get_image_url(filename):
    image_url = f"{BASE_URL}/image/{quote(filename)}"
    response = requests.get(image_url, headers={"Content-Type": "text"}, timeout=30)
    response.raise_for_status()
    return response.json()["image_url"]


def delete_image(filename):
    delete_url = f"{BASE_URL}/delete/{quote(filename)}"
    response = requests.delete(delete_url, timeout=30)
    response.raise_for_status()
    return response.json()


def get_filename_from_url(image_url):
    return Path(urlparse(image_url).path).name


def main():
    image_path = create_test_image()

    uploaded_url = upload_image(image_path)
    filename = get_filename_from_url(uploaded_url)
    received_url = get_image_url(filename)
    delete_response = delete_image(filename)

    print(f"POST /upload: {uploaded_url}")
    print(f"GET /image/{filename}: {received_url}")
    print(f"DELETE /delete/{filename}: {delete_response}")


if __name__ == "__main__":
    main()
