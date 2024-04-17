# Video Search via Pexels Script
- **Description**: Searches for videos using the Pexels API.
- **Requirements**:
  - PEXELS_API_KEY set as an environment variable.
  - Python packages: requests.
- **Usage**:
  - Provide the search term and the API key.
- **Output**:
  - Prints the ID, photographer, and URL of each video found.

# Text-to-Speech Generator Script
- **Description**: Converts text to speech using AWS Polly.
- **Requirements**:
  - AWS credentials set up in the environment (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN).
  - Python packages: boto3.
- **Usage**:
  - Provide the text, language, and output file name.
- **Output**:
  - Outputs the path to the saved audio file if successful.

# Image Search via Pexels Script
- **Description**: Searches for images using the Pexels API.
- **Requirements**:
  - PEXELS_API_KEY set as an environment variable.
  - Python packages: requests.
- **Usage**:
  - Provide the search term and the API key.
- **Output**:
  - Prints the ID, photographer, and URL of each image found.

# Read Telegram Messages Script
- **Description**: Reads messages from a Telegram bot and prints details such as conversation ID, message, author, and date.
- **Requirements**:
  - TELEGRAM_BOT_TOKEN set in the environment variable.
  - Python packages: python-telegram-bot.
- **Usage**:
  - Connect to a Telegram bot and process incoming messages.
- **Output**:
  - Prints the conversation ID, the message, the author, and the date of each message received by the bot.

# Send Telegram Message Script
- **Description**: Sends messages or files to a specified Telegram conversation.
- **Requirements**:
  - TELEGRAM_BOT_TOKEN set in the environment variable.
  - Python packages: python-telegram-bot.
- **Usage**:
  - Provide the chat ID and the message or file path to send.
- **Output**:
  - Prints the result of the message sent, including the message ID.
