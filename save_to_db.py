import asyncio

from steam_parser import get_cleaned_deals
from models import Game
from database import async_session

from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import update



async def main():
    async with async_session() as session:
        cleaned_deals = await get_cleaned_deals()
        reset_active_stmt = update(Game).values(is_active = False)
        await session.execute(reset_active_stmt)
        for game in cleaned_deals:
            new_game = insert(Game).values(
            steam_id=game["steam_id"],
            price_usd=game["price_usd"],
            discount_percent=game["discount_percent"],
            title=game["title"],
            url=game["url"],
            price_rub=game["price_rub"],
            price_kzt=game["price_kzt"],
            price_uah=game["price_uah"] 
            ).on_conflict_do_update(index_elements=[Game.steam_id], set_={"price_usd": game["price_usd"], "price_rub": game["price_rub"], "price_uah": game["price_uah"], "price_kzt": game["price_kzt"], "discount_percent": game["discount_percent"], "is_active": True})
            await session.execute(new_game)
        await session.commit()

if __name__ == "__main__":
    asyncio.run(main())