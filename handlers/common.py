import logging

from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from keyboards import get_main_kb, start_common_kb
from states import Profile

router = Router()


logger = logging.getLogger(__name__)

@router.message(F.text.lower().in_({"start 🚀", "start", "старт"}))
@router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Hi! Use my helpful bot for your own purposes! - Привет, используй моего полезного бота в своих целях?", reply_markup=start_common_kb())


@router.message(F.text.lower().in_({"info ℹ️", "info", "инфо", "информация"}))
@router.message(Command("info"))
async def info_handler(message: types.Message):
    await message.answer("Приветики, этот бот поможет тебе со скидками или бесплатными скидками в стим, ищи здесь свои любимые популярные игры по скидкам не нагружаясь самому в течении дня и не тратя свое время!")


@router.message(F.text.lower().in_({"назад", "back"}))
@router.message(Command("back"))
async def back_handler(message: types.Message, state: FSMContext):
    await message.answer("Ready!",reply_markup=get_main_kb())