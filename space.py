import requests
from pathlib import Path

from download_image import download_image


def fetch_spacex_last_launch(url, name_folder):
  response = requests.get(url)
  response.raise_for_status()
  images = response.json()
  for image in images:
    if image["links"]["flickr_images"]:
        flickr_images = image["links"]["flickr_images"]   
  for images_number, link_image in enumerate(flickr_images):
    filename = f"spacex{images_number}.jpg"
    file_path = f"{name_folder}/{filename}"
    download_image(link_image, file_path)


def main():
    name_folder = "images"
    Path(name_folder).mkdir(parents=True, exist_ok=True)
    url = "https://api.spacexdata.com/v3/launches"
    fetch_spacex_last_launch(url, name_folder)
    
    
  
if __name__ == "__main__":
  main()