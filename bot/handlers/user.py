from aiogram import Router, Bot
from aiogram.filters import CommandStart, Command

from aiogram.types import Message, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from aiogram_dialog import DialogManager, StartMode

from bot.states.user import ServiceCategoryDialogSG


router: Router = Router()


# Этот классический хэндлер будет срабатывать на команду /start
@router.message(CommandStart())
async def command_start_process(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(
        state=ServiceCategoryDialogSG.start,
        mode=StartMode.RESET_STACK,
        data={}
    )


@router.message(Command('blackout'))
async def command_balckout(message: Message, bot: Bot) -> None:
    markup = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text='Отключения', web_app=WebAppInfo(url='https://open.e-nkama.ru/shutdowns'))]],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await bot.send_message(chat_id=message.chat.id, text="Отключения", reply_markup=markup)
