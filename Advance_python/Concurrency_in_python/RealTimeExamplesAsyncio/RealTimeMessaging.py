#Listen and respond to messages from a queue asynchronously.

import asyncio
import random

async def producer(queue):
    for i in range(5):
        item = random.randint(1, 100)
        await queue.put(item)
        print(f"Produced: {item}")
        await asyncio.sleep(1)

async def consumer(queue):
    while True:
        item = await queue.get()
        print(f"Consumed: {item}")
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))

asyncio.run(main())
