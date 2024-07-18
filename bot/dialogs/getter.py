from aiogram_dialog import DialogManager

from lexicon.ru import Lexicon
from external_services.opencity_api.method import Blackout
from bot.dialogs.utils import _get_token
from config_data.config import Config, load_config


config: Config = load_config(".env")


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


async def data_blackout(dialog_manager: DialogManager, **kwarg) -> dict:
    data: dict = dialog_manager.start_data
    black_out = Blackout(
        apigate_url=config.api_opencity.apigate_url,
        api_token=await _get_token(),
        house_id=data['house_id']
    )
    print(data)
    print(await black_out.search())
    return {"items":()}
