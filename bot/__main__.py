from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Button, ScrollingGroup
from environs import Env


env = Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


class StartSG(StatesGroup):
    start = State()


class ServiceCategoryDialogSG(StatesGroup):
    first_page = State()
    second_page = State()
    third_page = State()
    fourth_page = State()


async def go_back(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.back()


async def go_next(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.next()


async def button_clicked(callback: CallbackQuery, button: Button, manager: DialogManager):
    await callback.message.answer('Кажется, ты нажал на кнопку!')


async def start_service_category(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=ServiceCategoryDialogSG.first_page)


def get_categories():
    return [
        "Крыша и водосточная система",
        "Чердак",
        "Подъезд",
        "Лифт",
        "Холодное водоснабжение",
        "Горячее водоснабжение",
        "Электроснабжение",
        "Подвал",
        "Фасад",
        "Мусор",
        "Мусоропровод",
        "Домофон",
        "Отопление",
        "Благоустройство",
        "Вентиляция",
        "Двор",
        "Дератизация",
        "Санитарная уборка",
        "Претензии к управляющей организации",
        "Электрическая плита",
        "Газоснабжение",
    ]


def test_buttons_creator(btn_quantity):
    buttons = []
    for i, item in enumerate(btn_quantity):
        buttons.append(Button(Const(item), id=f"{i}"))
    return buttons


async def some_getter(**kwargs):  # Здесь будем создавать нужные геттеры
    pass


# Это стартовый диалог
start_dialog = Dialog(
    Window(
        Const("📱Для того чтобы отправить заявку, выберите категорию и следуйте указаниям бота."),
        Button(
            text=Const('Оставить заявку'),
            id='button_submit_application',
            on_click=start_service_category),
        state=StartSG.start
    ),
)


service_category_dialog = Dialog(
    Window(
        Const(text='Выберите категорию:'),
        ScrollingGroup(
            *test_buttons_creator(get_categories()),
            id="numbers",
            width=1,
            height=6,
        ),
        state=ServiceCategoryDialogSG.first_page,
    ),
)


# Этот классический хэндлер будет срабатывать на команду /start
@dp.message(CommandStart())
async def command_start_process(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=StartSG.start, mode=StartMode.RESET_STACK)


if __name__ == '__main__':
    dp.include_routers(start_dialog, service_category_dialog)
    setup_dialogs(dp)
    dp.run_polling(bot)
