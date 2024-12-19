import asyncio
from tortoise import Tortoise
from db import TORTOISE_ORM

async def init():
    await Tortoise.init(config=TORTOISE_ORM)

if __name__ == "__main__":
    asyncio.run(init())

