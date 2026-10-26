import os
from dotenv import load_dotenv
from aiogram import Bot
load_dotenv()
ADMIN_ID = int(os.getenv("ADMIN_ID", 0))
TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)