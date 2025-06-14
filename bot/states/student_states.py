from aiogram.fsm.state import State, StatesGroup

class StudentStates(StatesGroup):
    start = State()
    send = State()
    default = State()