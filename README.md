# Text-to-Speech Generator Script
This script converts text to speech using AWS Polly. It is located at '/tmp/gptools/text_to_speech_generator.py'.
### Requirements:
- AWS credentials set up in the environment (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN).
- Python packages: boto3.
### Arguments:
1. Language code (e.g., 'en' for English, 'es' for Spanish).
2. Text message to convert.
3. Output filename for the generated speech file.
### Output:
- The script will output the path to the saved audio file if successful or an error message if not.
### Example:
`python text_to_speech_generator.py en 'Hello world' output.mp3


# Image Search via Pexels Script
This script searches for images using the Pexels API. It is located at /tmp/gptools/image_search_via_pexels.py.
### Requirements:
- Pexels API key set as an environment variable (PEXELS_API_KEY).
- Python packages: requests.
### Arguments:
1. Search term (e.g., cats).
2. Number of results per page.
### Output:
- The script will print the ID, photographer, and URL of each image found.
### Example:
python image_search_via_pexels.py cats 10

