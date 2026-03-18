import os
import requests

URL = "https://data.gov.ua/dataset/air-quality.csv"
OUTPUT_PATH = "data/raw/data.csv"


def download_data(url, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    response = requests.get(url)

    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        print("Data downloaded")
    else:
        print("Error downloading data")


if __name__ == "__main__":
    download_data(URL, OUTPUT_PATH)