from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import TextInput

from bot.states.user import ServiceCategoryDialogSG
from bot.dialogs import utils, window


main_dialog = Dialog(
    window.start,
    window.category,
    window.service,
    Window(
        Const("Введите название улицы"),
        TextInput(
            id='street_input',
            type_factory=utils.street_check,
            on_success=utils.correct_street_handler,
            on_error=utils.error_street_handler
        ),
        state=ServiceCategoryDialogSG.street
    ),
    Window(
        Const("Введите номер дома"),
        TextInput(
            id='house_input',
            type_factory=utils.house_check,
            on_success=utils.correct_house_handler,
            on_error=utils.error_house_handler
        ),
        state=ServiceCategoryDialogSG.house
    ),
    Window(
        Const("Введите номер квартиры"),
        TextInput(
            id='flat_input',
            type_factory=utils.flat_check,
            on_success=utils.correct_flat_handler,
            on_error=utils.error_flat_handler
        ),
        state=ServiceCategoryDialogSG.flat
    ),
    Window(
        Const("Введите ФИО"),
        TextInput(
            id='name_input',
            type_factory=utils.name_check,
            on_success=utils.correct_name_handler,
            on_error=utils.error_name_handler
        ),
        state=ServiceCategoryDialogSG.name
    ),
    Window(
        Const("Введите номер телефона"),
        TextInput(
            id='phone_input',
            type_factory=utils.phone_check,
            on_success=utils.correct_phone_handler,
            on_error=utils.error_phone_handler
        ),
        state=ServiceCategoryDialogSG.phone
    ),
    Window(
        Const("Опишите суть вашей проблемы"),
        TextInput(
            id='text_input',
            type_factory=utils.text_check,
            on_success=utils.correct_text_handler,
            on_error=utils.error_text_handler
        ),
        state=ServiceCategoryDialogSG.text
    ),
    Window(
        Const("Введите номер лицевого счёта"),
        TextInput(
            id='personal_account_input',
            type_factory=utils.personal_account_check,
            on_success=utils.correct_personal_account_handler,
            on_error=utils.error_personal_account_handler
        ),
        state=ServiceCategoryDialogSG.personal_account
    ),
    Window(
        Format("<b>Категория</b> - <i>{category}</i>"),
        Format("<b>Сервис</b> - <i>{service}</i>"),
        Format("<b>Улица</b> - <i>{street}</i>"),
        Format("<b>Дом</b> - <i>{house}</i>"),
        Format("<b>Квартира</b> - <i>{flat}</i>"),
        Format("<b>ФИО</b> - <i>{name}</i>"),
        Format("<b>Телефон</b> - <i>{phone}</i>"),
        Format("<b>Описание</b> - <i>{text}</i>"),
        Format("<b>Лицевой счёт</b> - <i>{personal_account}</i>"),
        Button(Const("Отправить заявку"), id="submit_application", on_click=utils.sent_application),
        state=ServiceCategoryDialogSG.application_form,
        getter=utils.data_getter
    ),
)
