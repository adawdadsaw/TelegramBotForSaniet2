from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='PS 4'),
            KeyboardButton(text='PS 4 pro'),
            KeyboardButton(text='PS 5'),
        ],

    ],
    resize_keyboard=True
)