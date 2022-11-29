import datetime
import os.path
from pathlib import Path
from pprint import pprint

import requests

#from download_image import download_image
def download_image(url, file_path, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)


def get_picture_EPIC(nasa_key, name_folder):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    params = {
      "api_key": nasa_key
    }
    response = requests.get(url, params=params)
    images_nasa = response.json()
    for number, image_nasa in enumerate(images_nasa):
        date_publish = image_nasa['date']
        name_image = image_nasa['image']
        image_date_format = datetime.datetime.fromisoformat(date_publish).strftime('%Y/%m/%d')
        
        image_url =   f"https://api.nasa.gov/EPIC/archive/natural/{image_date_format}/png/{name_image}.png"
        extension = determine_file_extension(image_url)
        filename = f"epic{number}{extension}"
        file_path = f"{name_folder}/{filename}"
        download_image(image_url, file_path, params)

    
def determine_file_extension(image_url):
    url, extension = os.path.splitext(image_url)
    return extension
    
    
def main():
    nasa_key = os.getenv("NASA_KEY")
    name_folder = "images"
    Path(name_folder).mkdir(parents=True, exist_ok=True)
    get_picture_EPIC(nasa_key, name_folder)
  
if __name__ == "__main__":
  main()


 


 


 