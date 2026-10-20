import asyncio
import logging

from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from states import Broadcast



router = Router()


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", filename="bot.log", encoding="utf-8")
logger = logging.getLogger(__name__)



@router.message(F.text.lower() == "sendall")
@router.message(Command("sendall"))
async def mailing_mode(message: types.Message, state: FSMContext, is_admin: bool):
    if is_admin:
        await state.set_state(Broadcast.text)
        await message.answer(f"{message.from_user.id} Жду контент для рассылки")
    else:
        await message.answer("Отказано в доступе")

@router.message(Command("cancel_sendall"), StateFilter(Broadcast.text))
@router.message(F.text.lower() == "cancel_sendall", StateFilter(Broadcast.text))
async def cancel_sendall(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Рассылка успешно отменена!")


@router.message(StateFilter(Broadcast.text))
async def mailing_logic(message: types.Message, state: FSMContext, db):
    users = await db.all_user_id()
    count = 0
    errors = 0
    for user in users:
        try:
            await message.copy_to(chat_id=user)
            count += 1
            await asyncio.sleep(0.05)
        except Exception as e:
            logger.error(f"Не удалось отправить {user}. Ошибка: {e}")
            errors += 1  
            
    await message.answer(f"Рассылка завершена! Получили: {count}, Не смогли получить: {errors}")
    await state.clear()