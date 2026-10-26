import os
import logging
import asyncio

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from config import bot
from handlers import common, discount_on_steam, settings
from middlewares.ThrottlingMiddleware import ThrottlingMiddleware

logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s", 
    filename="bot.log", 
    encoding="utf-8"
)

logger = logging.getLogger(__name__)

dp = Dispatcher()

async def main():
    dp.include_routers(common.router, discount_on_steam.router, settings.router)
    logger.info("Бот запущен и готов к работе")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())