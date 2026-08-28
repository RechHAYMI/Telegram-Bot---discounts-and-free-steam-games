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
        "title": deal["title"]
    }
    return clean_data


if __name__ == "__main__":
    result = asyncio.run(fetch_cheapshark_deals())
    cleaned_games = []

    for game in result:
        transform_game = transform_deal_data(game)
        cleaned_games.append(transform_game)
    #first_deal = result[0]
    print(cleaned_games)
    #pure_numbers = transform_deal_data(first_deal)
    #print(pure_numbers)