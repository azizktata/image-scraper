import os
import pandas as pd
import requests
from duckduckgo_search import DDGS
import time

country = "tunisie"
# Read Excel file
def read_excel(file_path):
    df = pd.read_excel(file_path, dtype=str)
    df = df[['Nom', 'Référence interne']].dropna()
    return [{'name': row['Nom'], 'reference': row['Référence interne']} for _, row in df.iterrows()]

# Search images using DuckDuckGo API
def search_images(query, max_results=4,retries=5, delay=5):
    for attempt in range(retries):
        try:
            results = DDGS().images(keywords=query+country, region="wt-wt", safesearch="on", max_results=max_results, size="Large", license_image=None,)
            if results:
                return [img['image'] for img in results]  
        except Exception as e:
            print(f"Error searching images for {query}: {attempt}")
            time.sleep(delay)
    return []

# Download image
def download_image(url, folder, filename):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            file_path = os.path.join(folder, filename)
            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Downloaded: {file_path}")
        else:
            print(f"Failed to download {url} (Status Code: {response.status_code})")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

# Sanitize filename
def sanitize_filename(name):
    return "".join(c if c.isalnum() or c in " _-" else "_" for c in name).strip()[:100]

# Process Excel file
def process_excel(file_path):
    data = read_excel(file_path)
    output_dir = "downloaded_images"
    os.makedirs(output_dir, exist_ok=True)

    for item in data:
        if not item['name'] or not item['reference']:
            print("Skipping invalid row:", item)
            continue

        search_query = f"{item['name']} {item['reference']}"
        print(f"Searching for: {search_query}")

        image_urls = search_images(search_query)
        safe_name = sanitize_filename(item['name'])
        safe_ref = sanitize_filename(item['reference'])
        item_folder = os.path.join(output_dir, f"{safe_name}_{safe_ref}")
        os.makedirs(item_folder, exist_ok=True)

        for i, img_url in enumerate(image_urls, start=1):
            download_image(img_url, item_folder, f"image_{item['reference']}_{i}.jpg")

# Run script
excel_file_path = "./articles.xlsx"
process_excel(excel_file_path)
