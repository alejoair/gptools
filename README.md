# GPTools Repository Documentation

## Scripts Overview

1. **Image Search via Pexels Script**
   - **Path**: /tmp/gptools/image_search_via_pexels.py
   - **Description**: Searches for images using the Pexels API.
   - **Requirements**:
     - PEXELS_API_KEY set as an environment variable.
     - Python packages: requests.
   - **Usage**: python image_search_via_pexels.py <search_term> <per_page>

2. **Read Telegram Messages Script**
   - **Path**: /tmp/gptools/read_telegram_messages.py
   - **Description**: Reads messages from a specified Telegram bot.
   - **Requirements**:
     - TELEGRAM_BOT_TOKEN set as an environment variable.
     - Python packages: python-telegram-bot.
   - **Usage**: python read_telegram_messages.py

3. **Send Telegram Message Script**
   - **Path**: /tmp/gptools/send_telegram_message.py
   - **Description**: Sends messages to a specified Telegram chat.
   - **Requirements**:
     - TELEGRAM_BOT_TOKEN set as an environment variable.
     - Python packages: python-telegram-bot.
   - **Usage**: python send_telegram_message.py <chat_id> <message>

4. **Text to Speech Generator Script**
   - **Path**: /tmp/gptools/text_to_speech_generator.py
   - **Description**: Converts text to speech using AWS Polly
   - **Requirements**:
     - AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY Environment variables 
     - Python packages: boto3.
   - **Usage**: python text_to_speech_generator.py <language_code> '<message>' <output_file> 

5. **Video Search via Pexels Script**
   - **Path**: /tmp/gptools/video_search_via_pexels.py
   - **Description**: Searches for videos using the Pexels API.
   - **Requirements**:
     - PEXELS_API_KEY set as an environment variable.
     - Python packages: requests.
   - **Usage**: python video_search_via_pexels.py <search_term> <per_page>

