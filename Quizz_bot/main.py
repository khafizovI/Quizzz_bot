import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from handlers import setup_handlers
from config import BOT_TOKEN
from tortoise import Tortoise
from db import TORTOISE_ORM


# Configure logging
logging.basicConfig(level=logging.INFO)


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="🎮 Botni boshlash"),
        BotCommand(command="quiz", description="📚 Viktorinani boshlash"),
        BotCommand(command="help", description="ℹ️ Yordam"),
        BotCommand(command="points", description="🏆 Ballarni ko'rish"),
        BotCommand(command="categories", description="📑 Kategoriyalar"),
    ]
    await bot.set_my_commands(commands)


async def main():
    # Initialize database
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()

    # Initialize bot and dispatcher
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    setup_handlers(dp)
    # Set bot commands
    await set_commands(bot)

    # Start message
    logging.info("Bot ishga tushdi...")

    try:
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Xatolik yuz berdi: {e}")
    finally:
        await bot.session.close()
        await Tortoise.close_connections()


if __name__ == "__main__":
    asyncio.run(main())
