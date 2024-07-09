from aiogram.types import CallbackQuery, Message

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import ManagedTextInput

from bot.data import get_categories, get_services


async def go_back(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
) -> None:
    await dialog_manager.back()


async def go_next(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
) -> None:
    await dialog_manager.next()


async def category_selection(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager, *args
) -> None:
    data: dict = dialog_manager.start_data
    category_id = int(callback.data)
    data["category_id"] = category_id
    category = get_categories()[category_id]
    data['category'] = category
    data['services'] = get_services()[category_id]
    dialog_manager.start_data.update(data)
    await dialog_manager.next()


def category_buttons_creator(btn_quantity)-> list:
    buttons: list = []
    for i, item in enumerate(btn_quantity):
        buttons.append(Button(Const(item), id=f"{i}", on_click=category_selection))
    return buttons


async def service_selection(
        callback: CallbackQuery, button: Button, dialog_manager: DialogManager, *args, **kwargs
) -> None:
    data: dict = dialog_manager.start_data
    service_id = int(callback.data.split(':')[-1])
    data['service_id'] = service_id
    for elem in data['services']:
        if elem[1] == service_id:
            data['service'] = elem[0]
            break
    dialog_manager.start_data.update(data)
    await dialog_manager.next()


async def data_getter(dialog_manager: DialogManager, **kwarg) -> dict:
    data = dialog_manager.start_data
    format_items = (
        ("Категория", data["category"]),
        ("Сервис", data["service"]),
        ("Улица", data["street"]),
        ("Дом", data["house"]),
        ("Квартира", data["flat"]),
        ("ФИО", data["name"]),
        ("Телефон", data["phone"]),
        ("Описание", data["text"]),
        ("Лицевой счёт", data["personal_account"]),
    )
    data["format_items"] = format_items
    return data


def street_check(text: str) -> str:
    return text


# Хэндлер, который сработает, если пользователь ввел корректный возраст
async def correct_street_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str) -> None:
    data: dict = dialog_manager.start_data
    data['street'] = text
    dialog_manager.start_data.update(data)
    await dialog_manager.next()


# Хэндлер, который сработает на ввод некорректного возраста
async def error_street_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        error: ValueError) -> None:
    await message.answer(
        text='Вы ввели некорректный возраст. Попробуйте еще раз'
    )


def house_check(text: str) -> str:
    return text


# Хэндлер, который сработает, если пользователь ввел корректный возраст
async def correct_house_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str) -> None:
    data: dict = dialog_manager.start_data
    data['house'] = text
    dialog_manager.start_data.update(data)
    await dialog_manager.next()


# Хэндлер, который сработает на ввод некорректного возраста
async def error_house_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        error: ValueError) -> None:
    await message.answer(
        text='Вы ввели некорректный возраст. Попробуйте еще раз'
    )


def flat_check(text: str) -> str:
    return text


# Хэндлер, который сработает, если пользователь ввел корректный возраст
async def correct_flat_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str) -> None:
    data: dict = dialog_manager.start_data
    data['flat'] = text
    dialog_manager.start_data.update(data)
    await dialog_manager.next()


# Хэндлер, который сработает на ввод некорректного возраста
async def error_flat_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        error: ValueError) -> None:
    await message.answer(
        text='Вы ввели некорректный возраст. Попробуйте еще раз'
    )


def name_check(text: str) -> str:
    return text


# Хэндлер, который сработает, если пользователь ввел корректный возраст
async def correct_name_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str) -> None:
    data: dict = dialog_manager.start_data
    data['name'] = text
    dialog_manager.start_data.update(data)
    await dialog_manager.next()


# Хэндлер, который сработает на ввод некорректного возраста
async def error_name_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        error: ValueError) -> None:
    await message.answer(
        text='Вы ввели некорректный возраст. Попробуйте еще раз'
    )


def phone_check(text: str) -> str:
    return text


# Хэндлер, который сработает, если пользователь ввел корректный возраст
async def correct_phone_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str) -> None:
    data: dict = dialog_manager.start_data
    data['phone'] = text
    dialog_manager.start_data.update(data)
    await dialog_manager.next()


# Хэндлер, который сработает на ввод некорректного возраста
async def error_phone_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        error: ValueError) -> None:
    await message.answer(
        text='Вы ввели некорректный возраст. Попробуйте еще раз'
    )


def text_check(text: str) -> str:
    return text


# Хэндлер, который сработает, если пользователь ввел корректный возраст
async def correct_text_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str) -> None:
    data: dict = dialog_manager.start_data
    data['text'] = text
    dialog_manager.start_data.update(data)
    await dialog_manager.next()


# Хэндлер, который сработает на ввод некорректного возраста
async def error_text_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        error: ValueError) -> None:
    await message.answer(
        text='Вы ввели некорректный возраст. Попробуйте еще раз'
    )


def personal_account_check(text: str) -> str:
    return text


# Хэндлер, который сработает, если пользователь ввел корректный возраст
async def correct_personal_account_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str) -> None:
    data: dict = dialog_manager.start_data
    data['personal_account'] = text
    dialog_manager.start_data.update(data)
    await dialog_manager.next()


# Хэндлер, который сработает на ввод некорректного возраста
async def error_personal_account_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        error: ValueError) -> None:
    await message.answer(
        text='Вы ввели некорректный возраст. Попробуйте еще раз'
    )


async def sent_application(callback: CallbackQuery, button: Button, dialog_manager: DialogManager
) -> None:
    data: dict = dialog_manager.start_data
    await callback.message.answer(
        text=
        "<b>Заявка принята.</b>\n"
        f"<b>Номер заявки</b> - <i>{data['category']}</i>\n"
        f"<b>Наименование Управляющей компании</b> - <i>{data['service']}</i>"
    )
    await dialog_manager.done()
