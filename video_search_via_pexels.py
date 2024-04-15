import os
import requests
import sys

def search_pexels_videos(search_term, per_page):
    api_key = os.getenv("PEXELS_API_KEY")
    if not api_key:
        print("API Key for Pexels is not set.")
        return
    url = "https://api.pexels.com/videos/search"
    headers = {"Authorization": api_key}
    params = {"query": search_term, "per_page": per_page}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        videos = response.json().get("videos", [])
        for video in videos:
            print(f"ID: {video['id']}, Author: {video['user']['name']}, URL: {video['url']}")
            print("Available Resolutions and Links:")
            for file in video['video_files']:
                print(f"{file['quality']}: {file['link']}")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python video_search_via_pexels.py <search_term> <per_page>")
        sys.exit(1)
    search_term = sys.argv[1]
    per_page = int(sys.argv[2])
    search_pexels_videos(search_term, per_page)
