from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

from enums import CallBacks, ButtonsText

data_confirmation_kb = [
    [InlineKeyboardButton(text=ButtonsText.confirm.value, callback_data=CallBacks.confirm.value),
    InlineKeyboardButton(text=ButtonsText.decline.value, callback_data=CallBacks.decline.value)]
]

data_confirmation_mk = InlineKeyboardMarkup(inline_keyboard=data_confirmation_kb)
