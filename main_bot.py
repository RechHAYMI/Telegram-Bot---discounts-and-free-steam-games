import os
import logging
import asyncio

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

from middlewares.main_middleware import ShadowMiddleware
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
    pool = await init_postgres()
    asyncio.create_task(shadow_parser(pool))
    await dp.start_polling(bot, pool=pool)
    logger.info("Бот запущен и готов к работе")

if __name__ == "__main__":
    asyncio.run(main())