from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_main_menu_buttons():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📚 Quizzes"), KeyboardButton(text="🏆 Points")],
            [KeyboardButton(text="ℹ️ Help"), KeyboardButton(text="🛍 Shop")],
        ],
        resize_keyboard=True
    )
    return keyboard


key_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛒 View Items")],
        [KeyboardButton(text="↩️ Back")]
    ],
    resize_keyboard=True
)


def get_quiz_menu_buttons():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🎯 Start Quiz"), KeyboardButton(text="📊 Leaderboard")],
            [KeyboardButton(text="📝 My Progress")],
            [KeyboardButton(text="↩️ Back")]
        ],
        resize_keyboard=True
    )
    return keyboard


def get_quiz_buttons(options):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=option)] for option in options],
        resize_keyboard=True
    )
    return keyboard
