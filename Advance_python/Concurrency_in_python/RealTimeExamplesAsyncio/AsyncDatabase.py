# Query a database concurrently using async libraries like aiomysql.

import aiomysql
import asyncio

async def query_database(query):
    conn = await aiomysql.connect(host="localhost", user="user", password="password", db="test")
    async with conn.cursor() as cursor:
        await cursor.execute(query)
        result = await cursor.fetchall()
        print(result)
    conn.close()

async def main():
    queries = ["SELECT * FROM table1", "SELECT * FROM table2"]
    await asyncio.gather(*(query_database(query) for query in queries))

asyncio.run(main())
