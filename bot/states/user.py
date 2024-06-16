from aiogram.fsm.state import State, StatesGroup


class StartSG(StatesGroup):
    start = State()


class ServiceCategoryDialogSG(StatesGroup):
    category = State()
    service = State()
    street = State()
    house = State()
    flat = State()
    personal_account = State()
    name = State()
    phone = State()
    text = State()
