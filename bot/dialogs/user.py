from aiogram.types import CallbackQuery

from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Button, ScrollingGroup, Select

from bot.states.user import StartSG, ServiceCategoryDialogSG
from bot.data import get_categories, get_services


async def go_back(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    await dialog_manager.back()


async def go_next(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    dialog_manager.dialog_data.update(callback_data=callback.data)
    await dialog_manager.next()


async def button_clicked(
    callback: CallbackQuery, button: Button, manager: DialogManager
):
    await callback.message.answer("Кажется, ты нажал на кнопку!")


async def start_service_category(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    await dialog_manager.start(state=ServiceCategoryDialogSG.category)


def category_buttons_creator(btn_quantity):
    buttons = []
    for i, item in enumerate(btn_quantity):
        buttons.append(Button(Const(item), id=f"{i}", on_click=go_next))
    return buttons


async def get_data(dialog_manager: DialogManager, **kwargs):
    return {'services': get_services()[int(dialog_manager.dialog_data.get("callback_data"))]}


# Это стартовый диалог
start_dialog = Dialog(
    Window(
        Const(
            "📱Для того чтобы отправить заявку, выберите категорию и следуйте указаниям бота."
        ),
        Button(
            text=Const("Оставить заявку"),
            id="button_submit_application",
            on_click=start_service_category,
        ),
        state=StartSG.start,
    ),
)


service_category_dialog = Dialog(
    Window(
        Const(text="Выберите категорию:"),
        ScrollingGroup(
            *category_buttons_creator(get_categories()),
            id="category",
            width=1,
            height=6,
        ),
        state=ServiceCategoryDialogSG.category,
    ),
    Window(
        Const(text="Выберите сервис:"),
        Button(Const("Вернуться"), id="back_to_category", on_click=go_back),
        ScrollingGroup(
            Select(
                Format('{item[0]}'),
                id='categ',
                item_id_getter=lambda x: x[1],
                items='services',
                #on_click=category_selection,
            ),
            id="service",
            width=1,
            height=6,
        ),
        state=ServiceCategoryDialogSG.service,
        getter=get_data,
    ),
)
