from contextlib import asynccontextmanager
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from save_to_db import main
from fastapi import FastAPI
import logging

logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s", 
    filename="bot.log", 
    encoding="utf-8"
)
logger = logging.getLogger(__name__)

scheduler = AsyncIOScheduler()

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        scheduler.add_job(
            main,
            trigger=IntervalTrigger(minutes=180),
            id='currency_update_job',
            replace_existing=True
        )
        scheduler.start()
        logger.info("Планировщик парсера и экспорт в базу данных запущен")
        yield
    except Exception as e:
        logger.error(f"Ошибка инициализации планировщика: {e}")
    finally:
        scheduler.shutdown()
        logger.info("Планировщик парсера и экспорт в базу данных закончен")