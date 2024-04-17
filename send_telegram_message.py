import asyncio
import os
import sys
import telegram

async def send_message_or_file(conversation_id, content):
    """
    Send a message or a file to a specified Telegram conversation.

    Args:
        conversation_id (str): The chat ID for the message.
        content (str): The text or path to the file to send.

    Returns:
        None
    """
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not token:
        print("TELEGRAM_BOT_TOKEN environment variable not set.")
        return

    bot = telegram.Bot(token)
    try:
        if os.path.isfile(content):
            with open(content, 'rb') as file:
                message = await bot.send_document(chat_id=conversation_id, document=file)
        else:
            message = await bot.send_message(chat_id=conversation_id, text=content)
        print("Message sent successfully:", message.message_id)
    except telegram.error.BadRequest as e:
        print("Failed to send message due to bad request:", str(e))
    except Exception as e:
        print("Failed to send message:", str(e))

if __name__ == '__main__':
    asyncio.run(send_message_or_file(sys.argv[1], sys.argv[2]))
