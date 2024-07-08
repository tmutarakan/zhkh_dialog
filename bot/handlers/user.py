from aiogram import Router
from aiogram.filters import CommandStart

from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from bot.states.user import StartSG


router: Router = Router()


# Этот классический хэндлер будет срабатывать на команду /start
@router.message(CommandStart())
async def command_start_process(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=StartSG.start, mode=StartMode.RESET_STACK)
