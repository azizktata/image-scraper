# Image Scraper from Excel using DuckDuckGo Search

#### Overview

This Python script reads product names and references from an Excel file, searches for related images using the DuckDuckGo Image Search API, and downloads them into organized folders.

#### Features

- Reads product data from an Excel file

- Searches for images using DuckDuckGo

- Downloads images into categorized folders

- Handles errors and retries failed requests

#### Requirements

- Ensure you have Python installed and install the required dependencies using:
  `pip install pandas requests duckduckgo-search openpyxl`

#### Usage

- Place your Excel file (articles.xlsx) in the script directory.

Run the script:

`python main.py`

Downloaded images will be stored in the downloaded_images/ directory, grouped by product name and reference.

#### File Structure

project-folder/
│── script.py # Main script
│── articles-test.xlsx # Input Excel file
│── downloaded_images/ # Output folder for images
│── README.md # Documentation

#### Configuration

- Modify max_results in search_images() to adjust the number of images fetched per product.

- Customize the search query by adding country-specific terms (e.g., Tunisie).

- Adjust the retry mechanism and delay settings in case of request failures.
