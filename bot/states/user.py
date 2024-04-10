from aiogram.fsm.state import State, StatesGroup


class StartSG(StatesGroup):
    start = State()


class ServiceCategoryDialogSG(StatesGroup):
    category = State()
    service = State()
