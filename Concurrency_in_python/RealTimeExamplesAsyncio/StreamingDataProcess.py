# Process a stream of data (e.g., real-time logs) using async for.

import asyncio

async def stream_logs():
    for i in range(10):
        yield f"Log entry {i}"
        await asyncio.sleep(1)

async def process_logs():
    async for log in stream_logs():
        print(f"Processed: {log}")

asyncio.run(process_logs())
