import sys
import requests
import time
import json
import os
from datetime import datetime
from utils import spinner

# Base URL for the API endpoint
BASE_URL = "https://www.4byte.directory/api/v1/signatures/"

# Directory to save the JSON files
OUTPUT_DIR = "./data"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# File to keep track of progress
PROGRESS_FILE = "./data/progress.txt"

def save_progress(page):
    with open(PROGRESS_FILE, 'w') as file:
        file.write(str(page))

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r') as file:
            return int(file.read())
    return 1  # Start from page 1 if no progress file exists

def fetch_total_pages():
    response = requests.get(BASE_URL, params={'format': 'json', 'ordering': 'created_at'})
    response.raise_for_status()  # This will raise an HTTPError for bad responses
    data = response.json()
    totalItems = data['count']
    totalPages = totalItems / 100 # 100 items per page
    # round up to the nearest whole number
    return int(totalPages) + 1
    
    

# Main function to fetch and save data
def fetch_data():
    page = load_progress()
    total_pages = fetch_total_pages()
    started_at = datetime.now()
    downloaded = 0
    if page > total_pages:
        print(f"No new pages to fetch. {total_pages}/{total_pages} already downloaded.")
        return

    print(f"Fetching data from page {page} to {total_pages}...")
    while page <= total_pages:
        params = {'page': page, 'format': 'json',  'ordering': 'created_at'}  # Ensure ascending order by ID
        try:
            response = requests.get(BASE_URL, params=params)
            response.raise_for_status()  # This will raise an HTTPError for bad responses

            data = response.json()
            if not data['results']:  # Break the loop if there are no results
                print("No more data to fetch.")
                break

            # Save the current page as a JSON file
            with open(f"{OUTPUT_DIR}/page_{page}.json", 'w') as json_file:
                json.dump(data, json_file, indent=4)
            
            # Print progress
            if downloaded > 0 and page % 10 == 0:
              eta = (datetime.now() - started_at) / downloaded * (total_pages - page)
              eta = str(eta).split(".")[0]
              print(f"  {spinner()} {page}/{total_pages} pages fetched and saved. ETA={eta}", end="\r", file=sys.stderr)
            if page % 1000 == 0:
              print(f"  ⚑ {page}/{total_pages} pages fetched and saved.")
            

            save_progress(page + 1)
            page += 1
            downloaded += 1

        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 429:  # Too Many Requests
                print("Rate limit exceeded. Sleeping for 5 seconds...")
                time.sleep(5)  # Wait a bit and try again
            else:
                print(f"HTTP error occurred: {e}")
                break  # Break the loop for other HTTP errors
        except Exception as e:
            print(f"An error occurred: {e}")
            break  # Break the loop for non-HTTP errors

        # time.sleep(0.01)

if __name__ == "__main__":
    fetch_data()
