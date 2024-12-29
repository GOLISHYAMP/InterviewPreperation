#Fetch stock prices from multiple APIs simultaneously.

import aiohttp
import asyncio

async def fetch_stock_price(session, stock):
    url = f"https://api.example.com/stock/{stock}"
    async with session.get(url) as response:
        data = await response.json()
        print(f"{stock}: {data['price']}")

async def main():
    stocks = ["AAPL", "GOOGL", "MSFT"]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_stock_price(session, stock) for stock in stocks]
        await asyncio.gather(*tasks)

asyncio.run(main())
