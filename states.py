from aiogram.fsm.state import StatesGroup, State

class Profile(StatesGroup):
    name = State()

class SettingsStates(StatesGroup):
    waiting_for_percent = State()

class Broadcast(StatesGroup):
    text = State()