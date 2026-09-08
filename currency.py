import httpx
import asyncio

async def fetch_exchange_rates():
    url = "https://open.er-api.com/v6/latest/USD"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    async with httpx.AsyncClient(headers=headers) as client:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            rates = data["rates"]
            return {"RUB": rates["RUB"], "KZT": rates["KZT"], "UAH": rates["UAH"]}