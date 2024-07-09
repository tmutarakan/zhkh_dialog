from aiogram import Router
from aiogram.filters import CommandStart

from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from bot.states.user import ServiceCategoryDialogSG


router: Router = Router()


# Этот классический хэндлер будет срабатывать на команду /start
@router.message(CommandStart())
async def command_start_process(message: Message, dialog_manager: DialogManager) -> None:
    data = {
        'category_id': '',
        'category': '',
        'services': '',
        'service_id': '',
        'service': '',
        'street': '',
        'house': '',
        'flat': '',
        'name': '',
        'phone': '',
        'text': '',
        'personal_account': ''
    }
    await dialog_manager.start(
        state=ServiceCategoryDialogSG.start,
        mode=StartMode.RESET_STACK,
        data=data)
