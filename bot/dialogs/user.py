from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format, List
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import TextInput

from bot.states.user import BlackoutDialogSG, ServiceCategoryDialogSG
from bot.dialogs import utils, window, getter
from lexicon.ru import Lexicon


main_dialog = Dialog(
    window.start,
    window.category,
    window.service,
    Window(
        Const(Lexicon.input_street),
        TextInput(
            id='street_input',
            type_factory=utils.address_check,
            on_success=utils.correct_street_handler,
        ),
        state=ServiceCategoryDialogSG.street
    ),
    Window(
        Const(Lexicon.input_house),
        TextInput(
            id='house_input',
            type_factory=utils.address_check,
            on_success=utils.correct_house_handler,
        ),
        state=ServiceCategoryDialogSG.house
    ),
        Window(
        Const(Lexicon.input_flat),
        TextInput(
            id='flat_input',
            type_factory=utils.address_check,
            on_success=utils.correct_flat_handler,
        ),
        state=ServiceCategoryDialogSG.flat
    ),
    Window(
        Const(Lexicon.input_name),
        TextInput(
            id='name_input',
            type_factory=utils.name_check,
            on_success=utils.correct_name_handler,
            on_error=utils.error_name_handler
        ),
        state=ServiceCategoryDialogSG.name
    ),
    Window(
        Const(Lexicon.input_phone),
        TextInput(
            id='phone_input',
            type_factory=utils.phone_check,
            on_success=utils.correct_phone_handler,
            on_error=utils.error_phone_handler
        ),
        state=ServiceCategoryDialogSG.phone
    ),
    Window(
        Const(Lexicon.input_text),
        TextInput(
            id='text_input',
            type_factory=utils.text_check,
            on_success=utils.correct_text_handler,
            on_error=utils.error_text_handler
        ),
        state=ServiceCategoryDialogSG.text
    ),
    Window(
        Const(Lexicon.input_personal_account),
        TextInput(
            id='personal_account_input',
            type_factory=utils.personal_account_check,
            on_success=utils.correct_personal_account_handler,
            on_error=utils.error_personal_account_handler
        ),
        state=ServiceCategoryDialogSG.personal_account
    ),
    Window(
        List(field=Format("<b>{item[0]}</b> - <i>{item[1]}</i>"), items="items"),
        Button(Const(Lexicon.sent_application), id="submit_application", on_click=utils.sent_application),
        state=ServiceCategoryDialogSG.application_form,
        getter=getter.data_before_submit
    ),
)


blackout_dialog = Dialog(
    Window(
        Const(Lexicon.input_street),
        TextInput(
            id='street_input',
            type_factory=utils.address_check,
            on_success=utils.correct_street_handler,
        ),
        state=BlackoutDialogSG.street
    ),
    Window(
        Const(Lexicon.input_house),
        TextInput(
            id='house_input',
            type_factory=utils.address_check,
            on_success=utils.correct_house_handler,
        ),
        state=BlackoutDialogSG.house
    ),
    Window(
        Const("output"),
        Button(Const("close"), id="close_blackout", on_click=utils.close_dialog),
        state=BlackoutDialogSG.output,
    ),
)
