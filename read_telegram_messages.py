"""This module uses the Telegram Bot API to read and print messages from a specified bot."""

import asyncio
import os
import telegram

async def main():
    """Main function to fetch and display messages from Telegram."""
    # Load the Telegram bot token from the environment variable
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not token:
        print("TELEGRAM_BOT_TOKEN environment variable not set.")
        return

    # Initialize the bot with the token
    bot = telegram.Bot(token)

    # Retrieve updates (messages sent to the bot)
    updates = await bot.get_updates()

    if not updates:
        print("No new messages.")
    else:
        # Process each update (message)
        for update in updates:
            # Extract message details
            message = update.message
            if message:
                print(f"Conversation ID: {message.chat.id}")
                print(f"Message: {message.text}")
                print(f"Author: {message.from_user.name if message.from_user else 'Unknown'}")
                print(f"Date: {message.date.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == '__main__':
    asyncio.run(main())
