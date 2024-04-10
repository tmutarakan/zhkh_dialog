#import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart

from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode, setup_dialogs

from bot.states.user import StartSG
from bot.config import load_config
from bot.dialogs.user import start_dialog, service_category_dialog


# Загружаем конфиг в переменную config
config = load_config("bot/.env")

bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


# Этот классический хэндлер будет срабатывать на команду /start
@dp.message(CommandStart())
async def command_start_process(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=StartSG.start, mode=StartMode.RESET_STACK)


async def main():
    """# Инициализируем логгер
    logger = logging.getLogger(__name__)
    # Конфигурируем логирование
    logging.basicConfig(
        filename="tbot.log",
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
        '[%(asctime)s] - %(name)s - %(message)s'
    )

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')"""

    dp.include_routers(start_dialog, service_category_dialog)
    setup_dialogs(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
