from aiogram.fsm.state import State, StatesGroup


class ServiceCategoryDialogSG(StatesGroup):
    start = State()
    category = State()
    service = State()
    street = State()
    house = State()
    flat = State()
    name = State()
    phone = State()
    text = State()
    personal_account = State()
    application_form = State()


class BlackoutDialogSG(StatesGroup):
    street = State()
    house = State()
    output = State()
