#When fetching data from multiple URLs, 
# asyncio can handle requests concurrently, 
# making the process faster.

import aiohttp
import asyncio

async def fetch_url(session, url):
    async with session.get(url) as response:
        data = await response.text()
        print(f"Fetched {url} with length {len(data)}")

async def main():
    urls = [
        "https://example.com",
        "https://openai.com",
        "https://python.org"
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        await asyncio.gather(*tasks)

asyncio.run(main())
