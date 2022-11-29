import requests
from pathlib import Path
from pprint import pprint
import os.path

from download_image import download_image


def get_picture_nasa_day(nasa_key, name_folder):
    url = "https://api.nasa.gov/planetary/apod"
    params = {
      "count": 30,
      "api_key": nasa_key
    }
  
    response = requests.get(url, params=params)
    images_nasa = response.json()
    for images_number, image_nasa in enumerate(images_nasa):
        if image_nasa["url"]:
            link_image = image_nasa["url"]
            extension = determine_file_extension(link_image)
            filename = f"nasa{images_number}{extension}"
            file_path = f"{name_folder}/{filename}"
            download_image(link_image, file_path)


def determine_file_extension(link_image):
    url, extension = os.path.splitext(link_image)
    return extension


def main():
    nasa_key = os.getenv("key")
    name_folder = "images"
    Path(name_folder).mkdir(parents=True, exist_ok=True)
    
    name_folder = "nasa"
    Path(name_folder).mkdir(parents=True, exist_ok=True)
    get_picture_nasa_day(nasa_key, name_folder)

  