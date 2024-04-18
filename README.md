# GPTools Repository Documentation

## Scripts Overview

1. **Video Search via Pexels Script**
   - **Path**: 
   - **Description**: Searches for videos using the Pexels API.
   - **Requirements**:
     - PEXELS_API_KEY set as an environment variable.
     - Python packages: requests.
   - **Usage**:
     -python3 /tmp/gptools/video_search_via_pexels.py 'nature' 10
   - **Output**:
     - Prints the ID, photographer, and URL of each video found.

2. **Text-to-Speech Generator Script**
   - **Path**: 
   - **Description**: Converts text to speech using AWS Polly.
   - **Requirements**:
     - AWS credentials set up in the environment.
     - Python packages: boto3.
   - **Usage**:
    -python3 /tmp/gptools/text_to_speech_generator.py 'en' 'Hello, world!' '/tmp/voice_en.mp3'
   - **Output**:
     - Outputs the path to the saved audio file if successful.

3. **Image Search via Pexels Script**
   - **Path**: 
   - **Description**: Searches for images using the Pexels API.
   - **Requirements**:
     - PEXELS_API_KEY set as an environment variable.
     - Python packages: requests.
   - **Usage**:
	-python3 /tmp/gptools/image_search_via_pexels.py 'mountains' 5

   - **Output**:
     - Prints the ID, photographer, and URL of each image found.

4. **Read Telegram Messages Script**
   - **Path**: 
   - **Description**: Reads messages from a Telegram bot and prints details.
   - **Requirements**:
     - TELEGRAM_BOT_TOKEN set in the environment variable.
     - Python packages: python-telegram-bot.
   - **Usage**:
	-python3 /tmp/gptools/read_telegram_messages.py

   - **Output**:
     - Prints the conversation ID, the message, the author, and the date of each message received.

5. **Send Telegram Message Script**
   - **Path**: 
   - **Description**: Sends messages or files to a specified Telegram conversation.
   - **Requirements**:
     - TELEGRAM_BOT_TOKEN set in the environment variable.
     - Python packages: python-telegram-bot.
   - **Usage**:
     -python3 /tmp/gptools/send_telegram_message.py 123456789 'Hello from the bot!'

   - **Output**:
     - Prints the result of the message sent, including the message ID.

