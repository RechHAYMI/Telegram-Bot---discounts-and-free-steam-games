from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData

class StartCallback(CallbackData, prefix="start"):
    name: str


def get_main_kb():
    buttons = [
        [KeyboardButton(text="Start 🚀"), KeyboardButton(text="Info ℹ️")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

def start_common_kb():
    buttons = [
        [KeyboardButton(text="Discount Steam")], [KeyboardButton(text="Settings ⚙️")],
        [KeyboardButton(text="Back")]                                    
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
