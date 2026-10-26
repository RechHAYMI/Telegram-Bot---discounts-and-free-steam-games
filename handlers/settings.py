import logging

from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from keyboards import get_settings_kb, get_main_kb
from states import SettingsStates

router = Router()

logger = logging.getLogger(__name__)