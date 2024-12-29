# Run periodic tasks asynchronously.

import asyncio

async def periodic_task():
    while True:
        print("Running periodic task...")
        await asyncio.sleep(5)

async def main():
    await asyncio.gather(periodic_task(), asyncio.sleep(20))  # Run for 20 seconds

asyncio.run(main())
