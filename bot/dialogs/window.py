from types import FunctionType

from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const, Format, List
from aiogram_dialog.widgets.kbd import Button, ScrollingGroup, Select
from aiogram_dialog.widgets.input import TextInput

from bot.states.user import ServiceCategoryDialogSG
from bot.data import get_categories
from bot.dialogs import utils


start = Window(
    Const(
        "📱Для того чтобы отправить заявку, выберите категорию и следуйте указаниям бота."
    ),
    Button(
        text=Const("Оставить заявку"),
        id="button_submit_application",
        on_click=utils.go_next,
    ),
    state=ServiceCategoryDialogSG.start,
)

category = Window(
    Const("Выберите категорию:"),
    ScrollingGroup(
        *utils.category_buttons_creator(get_categories()),
        id="category",
        width=1,
        height=6,
    ),
    state=ServiceCategoryDialogSG.category,
)

service = Window(
    Const("Проблема:"),
    Button(Const("Вернуться"), id="back_to_category", on_click=utils.go_back),
    ScrollingGroup(
        Select(
            Format('{item[0]}'),
            id='categ',
            item_id_getter=lambda x: x[1],
            items='services',
            on_click=utils.service_selection,
        ),
        id="service",
        width=1,
        height=6,
    ),
    state=ServiceCategoryDialogSG.service,
    getter=utils.data_getter,
)


def create_window(
        state: ServiceCategoryDialogSG,
        getter:FunctionType,
        last_text: str,
        button_text: str,
        button_id: str,
        input_id: str,
        type_factory: FunctionType,
        on_success: FunctionType,
        on_error: FunctionType,
) -> Window:
    return Window(
        List(
            field=Format('<b>{item[0]}</b> - <i>{item[1]}</i>'),
            items='format_items'
        ),
        Const(f"\n{last_text}"),
        Button(Const(f"{button_text}"), id=f"{button_id}", on_click=utils.go_back),
        TextInput(
            id=input_id,
            type_factory=type_factory,
            on_success=on_success,
            on_error=on_error,
        ),
        state=state,
        getter=getter
    )
