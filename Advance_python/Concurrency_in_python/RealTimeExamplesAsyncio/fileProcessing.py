# Process multiple large files concurrently using asyncio.

import asyncio

async def process_file(filename):
    async with aiofiles.open(filename, mode="r") as f:
        contents = await f.read()
        print(f"Processed {filename} with length {len(contents)}")

async def main():
    files = ["file1.txt", "file2.txt", "file3.txt"]
    tasks = [process_file(file) for file in files]
    await asyncio.gather(*tasks)

import aiofiles
asyncio.run(main())
