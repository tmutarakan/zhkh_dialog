import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from aiogram_dialog import setup_dialogs

from config_data.main_menu import set_main_menu
from config_data.config import load_config
from bot.handlers.user import router
from bot.dialogs.user import main_dialog, blackout_dialog

async def main():
    # Инициализируем логгер
    """logger = logging.getLogger(__name__)
    # Конфигурируем логирование
    logging.basicConfig(
        #filename="tbot.log",
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
        '[%(asctime)s] - %(name)s - %(message)s'
    )

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')"""
    print('Starting bot')

    # Загружаем конфиг в переменную config
    config = load_config(".env")

    bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    await set_main_menu(bot)
    dp.include_routers(router, main_dialog, blackout_dialog)
    setup_dialogs(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
