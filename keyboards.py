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

def get_settings_kb():
    buttons = [
        [KeyboardButton(text="10%")],[KeyboardButton(text="20%")],
        [KeyboardButton(text="30%")],[KeyboardButton(text="40%")],
        [KeyboardButton(text="50%")],[KeyboardButton(text="60%")],
        [KeyboardButton(text="70%")],[KeyboardButton(text="80%")],
        [KeyboardButton(text="90%")],[KeyboardButton(text="100%")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)