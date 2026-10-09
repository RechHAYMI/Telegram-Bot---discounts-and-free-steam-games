import uvicorn

from fastapi import FastAPI, Depends
from sqlalchemy import select
from pydantic import BaseModel
from database import async_session
from sqlalchemy.ext.asyncio import AsyncSession
from models import Game

app = FastAPI()

class GameResponse( BaseModel ):
    title: str
    price_rub: float
    price_kzt: float
    price_usd: float
    price_uah: float
    discount_percent: int
    url: str

async def get_db():
    async with async_session() as session:
        yield session

@app.get("/discount")
async def get_discount(db: AsyncSession = Depends(get_db)):
    game_response = await db.scalars(select(Game).filter(Game.is_active == True))
    return game_response.all()