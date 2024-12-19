from aiogram import Dispatcher
from handlers import shop_router, quiz_router

def setup_handlers(dp: Dispatcher):
    dp.include_router(quiz_router.router)
    dp.include_router(shop_router.router)
