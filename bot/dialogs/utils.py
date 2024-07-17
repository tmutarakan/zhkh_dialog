import re

from aiogram.types import CallbackQuery, Message

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import ManagedTextInput

from bot.data import get_categories, get_services
from lexicon.ru import Lexicon
from external_services.opencity_api import model
from external_services.opencity_api.method import Check, create_token, Search, Issue
from config_data.config import Config, load_config


config: Config = load_config(".env")


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
    data['service_code'] = service_id
    for elem in data['services']:
        if elem[1] == service_id:
            data['service'] = elem[0]
            break
    dialog_manager.start_data.update(data)
    await dialog_manager.next()


async def data_getter(dialog_manager: DialogManager, **kwarg) -> dict:
    return dialog_manager.start_data


async def data_before_submit(dialog_manager: DialogManager, **kwarg) -> dict:
    data: dict = dialog_manager.start_data
    return {"items": (
            (Lexicon.category, data["category"]),
            (Lexicon.service, data["service"]),
            (Lexicon.street, data["street"]),
            (Lexicon.house, data["house"]),
            (Lexicon.flat, data["flat"]),
            (Lexicon.name, data["name"]),
            (Lexicon.phone, data["phone"]),
            (Lexicon.text, data["text"]),
            (Lexicon.personal_account, data["personal_account"])
        )
    }


def address_check(text: str) -> str:
    return text


async def _get_token() -> str:
    response = model.CreateTokenReturn(
        **await create_token(
            authentication_url=config.api_opencity.authentication_url,
            login=config.api_opencity.login,
            password=config.api_opencity.password
        )
    )
    return response.result.token


async def correct_street_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str) -> None:
    search = Search(
        apigate_url=config.api_opencity.apigate_url,
        api_token=await _get_token(),
        street=text)
    response = model.SearchStreetReturn(**await search.search_street())
    if response.result.items:
        data: dict = dialog_manager.start_data
        data['street'] = text
        dialog_manager.start_data.update(data)
        await dialog_manager.next()
    else:
        await message.answer(
            text=Lexicon.not_found_input_street
        )


async def correct_house_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str) -> None:
    data: dict = dialog_manager.start_data
    search = Search(
        apigate_url=config.api_opencity.apigate_url,
        api_token=await _get_token(),
        street=data['street'],
        house_number=text)
    response = model.SearchHouseReturn(**await search.search_house())
    if response.result.items:
        data['house'] = text
        dialog_manager.start_data.update(data)
        await dialog_manager.next()
    else:
        await message.answer(
            text=Lexicon.not_found_input_house
        )


async def correct_flat_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str) -> None:
    data: dict = dialog_manager.start_data
    search = Search(
        apigate_url=config.api_opencity.apigate_url,
        api_token=await _get_token(),
        street=data['street'],
        house_number=data['house'],
        flat_number=text)
    response = model.SearchFlatReturn(**await search.search_flat())
    if response.result.items:
        data['flat'] = text
        data['flat_id'] = response.result.items[0].id
        dialog_manager.start_data.update(data)
        await dialog_manager.next()
    else:
        await message.answer(
            text=Lexicon.not_found_input_flat
        )


def name_check(text: str) -> str:
    if len(text) <= 128:
        return text
    raise ValueError


async def correct_name_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str) -> None:
    data: dict = dialog_manager.start_data
    data['name'] = text
    dialog_manager.start_data.update(data)
    await dialog_manager.next()


async def error_name_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        error: ValueError) -> None:
    await message.answer(
        text=Lexicon.error_input_name
    )


def phone_check(text: str) -> str:
    if re.fullmatch(r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$", text):
        return text
    raise ValueError


async def correct_phone_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str) -> None:
    data: dict = dialog_manager.start_data
    data['phone'] = text
    dialog_manager.start_data.update(data)
    await dialog_manager.next()


async def error_phone_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        error: ValueError) -> None:
    await message.answer(
        text=Lexicon.error_input_phone
    )


def text_check(text: str) -> str:
    return text


async def correct_text_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str) -> None:
    data: dict = dialog_manager.start_data
    data['text'] = text
    dialog_manager.start_data.update(data)
    await dialog_manager.next()


async def error_text_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        error: ValueError) -> None:
    await message.answer(
        text=Lexicon.error_input_text
    )


def personal_account_check(text: str) -> str:
    if len(text)==10 and text.isdigit():
        return text
    raise ValueError


async def correct_personal_account_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str) -> None:
    data: dict = dialog_manager.start_data
    check = Check(
        apigate_url=config.api_opencity.apigate_url,
        api_token=await _get_token(),
        flat_id=data['flat_id'],
        personal_account=text
    )
    response = model.CheckPersonalAccountReturn(**await check.check_personal_account())
    if response.result:
        data['personal_account'] = text
        dialog_manager.start_data.update(data)
        await dialog_manager.next()
    else:
        await message.answer(
        text=Lexicon.error_personal_account
    )


async def error_personal_account_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        error: ValueError) -> None:
    await message.answer(
        text=Lexicon.error_input_personal_account
    )


async def sent_application(callback: CallbackQuery, button: Button, dialog_manager: DialogManager
) -> None:
    data: dict = dialog_manager.start_data
    issue = Issue(
        apigate_url=config.api_opencity.apigate_url,
        api_token=await _get_token(),
        fullname=data["name"],
        personal_account=data["personal_account"],
        service=data["service_code"],
        text=data["text"],
        building="-",
        flat=data["flat"],
        house=data["house"],
        phone=data["phone"],
        street=data["street"]
    )
    response = model.IssueCreateReturn(**await issue.create_request())
    print(response)
    await callback.message.answer(
        text=
        f"<b>{Lexicon.accepted}</b>\n"
        f"<b>{Lexicon.application_number}</b> - <i>{response.result.number}</i>\n"
        f"<b>{Lexicon.control_name}</b> - <i>{response.result.provider[0].providerName}</i>"
    )
    await dialog_manager.done()
