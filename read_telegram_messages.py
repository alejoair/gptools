import asyncio
import os
import telegram

async def fetch_and_display_messages():
    """Fetch messages from a specified Telegram bot and handle media downloads."""
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not token:
        print("TELEGRAM_BOT_TOKEN environment variable not set.")
        return

    bot = telegram.Bot(token)
    updates = await bot.get_updates()

    if not updates:
        print("No new messages.")
        return

    for update in updates:
        await process_message(update, bot)

async def process_message(update, bot):
    """Process individual messages and download media if present."""
    message = update.message
    if message:
        display_message_info(message)
        await handle_media_download(message, bot)

def display_message_info(message):
    """Display information about the message."""
    print(f"Conversation ID: {message.chat.id}")
    print(f"Message: {message.text}")
    print(f"Author: {message.from_user.name if message.from_user else 'Unknown'}")
    print(f"Date: {message.date.strftime('%Y-%m-%d %H:%M:%S')}")

async def handle_media_download(message, bot):
    """Download photos and documents associated with a message."""
    if message.photo:
        await download_photo(message.photo[-1].file_id, bot)
    if message.document:
        await download_document(message.document.file_id, message.document.file_name, bot)

async def download_photo(file_id, bot):
    """Download photo from message."""
    photo_file = await bot.get_file(file_id)
    await photo_file.download(custom_path=f"/tmp/{file_id}.jpg")
    print(f"Photo downloaded: /tmp/{file_id}.jpg")

async def download_document(file_id, file_name, bot):
    """Download document from message."""
    doc_file = await bot.get_file(file_id)
    file = await bot.getFile(doc_file.file_id)
    await doc_file.download_to_drive(custom_path=f"/tmp/{file_name if doc_file.file_path else file_id}")
    print(f"Document downloaded: /tmp/{file_id}{file_name}")

if __name__ == '__main__':
    asyncio.run(fetch_and_display_messages())
