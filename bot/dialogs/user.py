from pprint import pprint

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
    await dialog_manager.next()


async def start_service_category(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    await dialog_manager.start(state=ServiceCategoryDialogSG.category)


def category_buttons_creator(btn_quantity):
    buttons = []
    for i, item in enumerate(btn_quantity):
        buttons.append(Button(Const(item), id=f"{i}", on_click=category_selection))
    return buttons


async def get_data(dialog_manager: DialogManager, **kwargs):
    my_dialog_data = dialog_manager.dialog_data.get("my_dialog_data")
    category_id = int(my_dialog_data['category_id'])
    category = get_categories()[category_id]
    my_dialog_data['category'] = category
    return {
        'category': category,
        'services': get_services()[category_id]
    }

async def category_selection(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager, *args
):
    my_dialog_data = {"category_id": callback.data}
    dialog_manager.dialog_data.update(my_dialog_data=my_dialog_data)
    await dialog_manager.next()


async def service_selection(
        callback: CallbackQuery, button: Button, dialog_manager: DialogManager, *args, **kwargs
):
    my_dialog_data = dialog_manager.dialog_data.get("my_dialog_data")
    service_id = int(callback.data.split(':')[-1])
    my_dialog_data['service_id'] = service_id
    category_id = int(my_dialog_data['category_id'])
    services = get_services()[category_id]
    for elem in services:
        if elem[1] == service_id:
            my_dialog_data['service'] = elem[0]
            break
    dialog_manager.dialog_data.update(my_dialog_data=my_dialog_data)
    await dialog_manager.next()


async def username_getter(dialog_manager: DialogManager, **kwargs):
    return dialog_manager.dialog_data.get("my_dialog_data")


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
        Const("Выберите категорию:"),
        ScrollingGroup(
            *category_buttons_creator(get_categories()),
            id="category",
            width=1,
            height=6,
        ),
        state=ServiceCategoryDialogSG.category,
    ),
    Window(
        Format("<b>Категория</b> - <i>{category}</i>"),
        Const("Выберите сервис:"),
        Button(Const("Вернуться"), id="back_to_category", on_click=go_back),
        ScrollingGroup(
            Select(
                Format('{item[0]}'),
                id='categ',
                item_id_getter=lambda x: x[1],
                items='services',
                on_click=service_selection,
            ),
            id="service",
            width=1,
            height=6,
        ),
        state=ServiceCategoryDialogSG.service,
        getter=get_data,
    ),
    Window(
        Format("<b>Категория</b> - <i>{category}</i>"),
        Format("<b>Сервис</b> - <i>{service}</i>"),
        Const("\n"),
        Const("Введите название улицы"),
        Button(Const("Вернуться"), id="back_to_service", on_click=go_back),
        state=ServiceCategoryDialogSG.street,
        getter=username_getter
    ),
    Window(
        Format('Введите номер дома'),
        Button(Const("Вернуться"), id="back_to_category", on_click=go_back),
        state=ServiceCategoryDialogSG.house
    ),
    Window(
        Format('Введите номер квартиры'),
        Button(Const("Вернуться"), id="back_to_category", on_click=go_back),
        state=ServiceCategoryDialogSG.flat
    ),
    Window(
        Format('Введите ФИО'),
        Button(Const("Вернуться"), id="back_to_category", on_click=go_back),
        state=ServiceCategoryDialogSG.name
    ),
    Window(
        Format('Нажмите на кнопку ниже, чтобы отправить контакт'),
        Button(Const("Вернуться"), id="back_to_category", on_click=go_back),
        state=ServiceCategoryDialogSG.phone
    ),
    Window(
        Format('Опишите суть вашей проблемы'),
        Button(Const("Вернуться"), id="back_to_category", on_click=go_back),
        state=ServiceCategoryDialogSG.text
    ),
    Window(
        Format('Введите номер лицевого счёта'),
        Button(Const("Вернуться"), id="back_to_category", on_click=go_back),
        state=ServiceCategoryDialogSG.personal_account
    ),
)
