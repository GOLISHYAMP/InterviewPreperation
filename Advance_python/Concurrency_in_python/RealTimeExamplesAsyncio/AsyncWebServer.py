# Create a simple web server using asyncio.
from aiohttp import web

async def handle(request):
    name = request.query.get("name", "World")
    return web.Response(text=f"Hello, {name}!")

app = web.Application()
app.router.add_get("/", handle)

web.run_app(app)
