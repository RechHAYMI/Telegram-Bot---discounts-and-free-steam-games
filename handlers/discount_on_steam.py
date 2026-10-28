import logging

from aiogram import Router, types, F

from keyboards import get_main_kb, get_settings_kb

router = Router()

logger = logging.getLogger(__name__)

@router.message(F.text.lower().in_({"10", "10%", "20", "20%", "30", "30%", "40", "40%", "50", "50%", "60", "60%", "70", "70%", "80", "80%", "90", "90%", "100", "100%"}))
async def handle_discount(message: types.Message):
    discount = int(message.text.rstrip("%"))