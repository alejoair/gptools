import os
import requests
import sys

def search_pexels(search_term, per_page):
    api_key = os.getenv("PEXELS_API_KEY")
    if not api_key:
        print("API Key for Pexels is not set.")
        return
    url = "https://api.pexels.com/v1/search"
    headers = {"Authorization": api_key}
    params = {"query": search_term, "per_page": per_page}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        photos = response.json().get("photos", [])
        for photo in photos:
            print(f"ID: {photo['id']}, Autor: {photo['photographer']}, URL: {photo['src']['original']}")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pexels_search.py <search_term> <per_page>")
        sys.exit(1)
    search_term = sys.argv[1]
    per_page = int(sys.argv[2])
    search_pexels(search_term, per_page)
