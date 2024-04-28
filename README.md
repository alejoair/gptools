# GPTools Repository Documentation

This repository contains several scripts that interface with various APIs for tasks such as image and video search, sending messages, and text to speech conversion.

## Scripts Overview





### Text to Speech Generator Script
- **Script Name**: text_to_speech_generator.py
- **Description**: This script converts text to speech using AWS Polly. It requires AWS credentials set as environment variables.
- **Usage**:
  1. Convert simple text to speech: 'python /tmp/gptools/text_to_speech_generator.py 'Hello world' /tmp/hello.mp3'
  2. Convert text file content to speech: 'python /tmp/gptools/text_to_speech_generator.py  /tmp/output.mp3'
  3. Convert text with specified voice: 'python /tmp/gptools/text_to_speech_generator.py 'Hello again' /tmp/hello.mp3 --voice Joanna'


### Video Search via Pexels Script
- **Script Name**: video_search_via_pexels.py
- **Description**: This script allows users to search for videos via the Pexels API. It requires an API key set as an environment variable.
- **Usage**:
  1. Search for nature videos: 'python /tmp/gptools/video_search_via_pexels.py nature 10'
  2. Search for city videos: 'python /tmp/gptools/video_search_via_pexels.py city 5'
  3. Search for animal videos: 'python /tmp/gptools/video_search_via_pexels.py animals 20'


  3. Search for animal photographs: 'python /tmp/gptools/image_search_via_pexels.py animals 20'


### Image Search via Pexels Script
- **Script Name**: image_search_via_pexels.py
- **Description**: This script allows users to search for images via the Pexels API. It requires the 'PEXELS_API_KEY' environment variable to be set.
- **Environment Variable**: 'PEXELS_API_KEY'
- **Usage**:
  1. Search for nature images: 'python /tmp/gptools/image_search_via_pexels.py nature 10'
  2. Search for city landscapes: 'python /tmp/gptools/image_search_via_pexels.py city 5'
  3. Search for animal photographs: 'python /tmp/gptools/image_search_via_pexels.py animals 20'


### Read Telegram Messages Script
- **Script Name**: read_telegram_messages.py
- **Description**: This script allows users to read messages from a specified Telegram bot. It requires the 'TELEGRAM_BOT_TOKEN' environment variable to be set.
- **Environment Variable**: 'TELEGRAM_BOT_TOKEN'
- **Usage**:
  1. Read messages from default bot: 'python /tmp/gptools/read_telegram_messages.py'
  2. Continuously check for new messages: 'python /tmp/gptools/read_telegram_messages.py --continuous'
  3. Log messages to a file: 'python /tmp/gptools/read_telegram_messages.py --log /path/to/logfile.txt'


### Send Telegram Message Script
- **Script Name**: send_telegram_message.py
- **Description**: This script allows users to send messages or files to a specified Telegram chat. It is designed to work with Telegram's API and requires the 'TELEGRAM_BOT_TOKEN' environment variable to be set.
- **Environment Variable**: 
- **Usage**:
  1. Send a text message: 'python /tmp/gptools/send_telegram_message.py 123456789 'Hello, world!''
  2. Send a document: 'python /tmp/gptools/send_telegram_message.py 123456789 /path/to/document.pdf'
  3. Send an image: 'python /tmp/gptools/send_telegram_message.py 123456789 /path/to/image.jpg'


