# Video Search via Pexels Script
This script searches for videos using the Pexels API. It is located at /tmp/gptools/video_search_via_pexels.py.
### Requirements:
- Pexels API key set as an environment variable (PEXELS_API_KEY).
- Python packages: requests.
### Arguments:
1. Search term (e.g., 'nature').
2. Number of results per page.
### Output:
- The script will print the ID, photographer, and URL of each video found.
### Example:
python video_search_via_pexels.py 'nature' 10
