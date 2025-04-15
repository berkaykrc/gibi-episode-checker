"""
This module contains functions for sending notifications about new episodes to a Telegram channel.
"""
import os
import telegram
from dotenv import load_dotenv

load_dotenv()

async def send_telegram_notification(episode):
    """
    Send a notification to a Telegram channel about the new episodes.

    Args:
        new_episodes (list): A list of new episodes found.

    Returns:
        None
    """
    bot = telegram.Bot(token=os.getenv("token"))
    message = f"New episode available: {episode['title']}\nMagnet link: {episode['magnet_link']}"
    await bot.send_message(chat_id="@gibinewepisode", text=message)
