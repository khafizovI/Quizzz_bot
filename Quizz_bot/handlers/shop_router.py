from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from button import get_main_menu_buttons, key_menu
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


router = Router()


@router.message(F.text == "🛍 Shop")
async def show_shop_menu(message: types.Message):
    await message.answer(
        "Shop menyusi:",
        reply_markup=key_menu
    )


@router.message(lambda message: message.text == "↩️ Back")
async def back_to_main_menu(message: types.Message, state: FSMContext):
    await message.answer(
        "Asosiy menyu:",
        reply_markup=get_main_menu_buttons()
    )

@router.message(lambda message: message.text == "🛒 View Items")
async def show_items(message: types.Message):
    await message.answer("Items menu:")
    await message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQtiJ4qu6JI-D5CCnR1H6KrYulPeDKoSGgA-g&s",
        caption="1st Item\nPoints Required: 100\nDescription: A great product available for exchange."
    )
    await message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQtiJ4qu6JI-D5CCnR1H6KrYulPeDKoSGgA-g&s",
        caption="2nd Item\nPoints Required: 200\nDescription: A great product available for exchange."
    )
    await message.answer_photo(
        photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQtiJ4qu6JI-D5CCnR1H6KrYulPeDKoSGgA-g&s",
        caption="3rd Item\nPoints Required: 300\nDescription: A great product available for exchange."
    )


