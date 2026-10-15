from aiogram.fsm.state import StatesGroup, State

class Profile(StatesGroup):
    name = State()