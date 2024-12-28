#An asynchronous chat server can handle 
# multiple clients simultaneously without blocking.

import asyncio

async def handle_client(reader, writer):
    address = writer.get_extra_info("peername")
    print(f"Connection from {address}")
    while True:
        data = await reader.read(100)
        if not data:
            break
        message = data.decode()
        print(f"Received {message} from {address}")
        writer.write(data.upper().encode())
        await writer.drain()
    writer.close()

async def main():
    server = await asyncio.start_server(handle_client, "127.0.0.1", 8888)
    async with server:
        await server.serve_forever()

asyncio.run(main())
