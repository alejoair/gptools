# GPTools Repository Documentation

## Scripts Overview

1. **Video Search via Pexels Script**
   - **Path**: 
   - **Description**: Searches for videos using the Pexels API.
   - **Requirements**:
     - PEXELS_API_KEY set as an environment variable.
     - Python packages: requests.
   - **Usage**:
     - Usage: python video_search_via_pexels.py <search_term> <per_page>
   - **Output**:
     - Prints the ID, photographer, and URL of each video found.

2. **Text-to-Speech Generator Script**
   - **Path**: 
   - **Description**: Converts text to speech using AWS Polly.
   - **Requirements**:
     - AWS credentials set up in the environment.
     - Python packages: boto3.
   - **Usage**:
     - An error occurred: Unsupported language 'language code'. Supported languages are: ['es', 'en']
   - **Output**:
     - Outputs the path to the saved audio file if successful.

3. **Image Search via Pexels Script**
   - **Path**: 
   - **Description**: Searches for images using the Pexels API.
   - **Requirements**:
     - PEXELS_API_KEY set as an environment variable.
     - Python packages: requests.
   - **Usage**:
     - Usage: python pexels_search.py <search_term> <per_page>
   - **Output**:
     - Prints the ID, photographer, and URL of each image found.

4. **Read Telegram Messages Script**
   - **Path**: 
   - **Description**: Reads messages from a Telegram bot and prints details.
   - **Requirements**:
     - TELEGRAM_BOT_TOKEN set in the environment variable.
     - Python packages: python-telegram-bot.
   - **Usage**:
     - Conversation ID: 5818030164
Message: /start
Author: Alejo
Date: 2024-04-17 22:37:20
Conversation ID: 5818030164
Message: hi
Author: Alejo
Date: 2024-04-17 22:37:22
Conversation ID: 5818030164
Message: quiero que me mandes un saludo desde gpterminal
Author: Alejo
Date: 2024-04-18 02:07:33
   - **Output**:
     - Prints the conversation ID, the message, the author, and the date of each message received.

5. **Send Telegram Message Script**
   - **Path**: 
   - **Description**: Sends messages or files to a specified Telegram conversation.
   - **Requirements**:
     - TELEGRAM_BOT_TOKEN set in the environment variable.
     - Python packages: python-telegram-bot.
   - **Usage**:
     - Failed to send message due to bad request: Chat not found
   - **Output**:
     - Prints the result of the message sent, including the message ID.

