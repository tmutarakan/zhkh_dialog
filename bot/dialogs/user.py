from aiogram.types import CallbackQuery

from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Button, ScrollingGroup

from bot.states.user import StartSG, ServiceCategoryDialogSG
from bot.data import get_categories, get_services


async def go_back(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.back()


async def go_next(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.next()


async def button_clicked(callback: CallbackQuery, button: Button, manager: DialogManager):
    await callback.message.answer('Кажется, ты нажал на кнопку!')


async def start_service_category(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=ServiceCategoryDialogSG.category)


def test_buttons_creator(btn_quantity):
    buttons = []
    for i, item in enumerate(btn_quantity):
        buttons.append(
            Button(
                Const(item),
                id=f"{i}",
                on_click=go_next
                )
            )
    return buttons


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
            id="category",
            width=1,
            height=6,
        ),
        state=ServiceCategoryDialogSG.category,
    ),
    Window(
        Const(text='Выберите сервис:'),
        ScrollingGroup(
            *test_buttons_creator(get_services()),
            id="service",
            width=1,
            height=6,
        ),
        state=ServiceCategoryDialogSG.service,
    ),
)
