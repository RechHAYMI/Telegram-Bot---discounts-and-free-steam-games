import httpx
import asyncio

async def fetch_cheapshark_deals():
    url = "https://www.cheapshark.com/api/1.0/deals"
    params = {
        "storeID": 1,
        "onSale": 1,
        "sortBy": "Deal Rating",
        "metacritic": 75
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    async with httpx.AsyncClient(headers=headers) as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    

def transform_deal_data(deal: dict):
    clean_data = {
        "steam_id": int(deal["steamAppID"]),
        "price_usd": float(deal["salePrice"]),
        "discount_percent": int(float(deal["savings"])),
        "title": deal["title"],
        "url": f"https://store.steampowered.com/app/{deal['steamAppID']}/",
        "price_rub": 0.0,
        "price_kzt": 0.0,
        "price_uah": 0.0
    }
    return clean_data

async def get_cleaned_deals():
    result = await fetch_cheapshark_deals()
    cleaned_games = []
    for game in result:
        transform_game = transform_deal_data(game)
        cleaned_games.append(transform_game)
    print(cleaned_games)
    return cleaned_games

if __name__ == "__main__":
    asyncio.run(get_cleaned_deals())