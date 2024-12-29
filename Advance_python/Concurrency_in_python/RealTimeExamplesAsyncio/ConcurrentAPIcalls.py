# Make multiple asynchronous API calls and aggregate results.

import aiohttp
import asyncio

async def fetch_data(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3"
    ]
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*(fetch_data(session, url) for url in urls))
        for result in results:
            print(result)

asyncio.run(main())
