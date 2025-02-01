from aiogram.methods import DeleteWebhook

from tgbot_admin.bot.loader import dp, bot
from tgbot_admin.bot.data.config import SKIP_UPDATES
from tgbot_admin.bot.utils.logging import logger

from tgbot_admin.bot.app.handlers import setup_handlers
from tgbot_admin.bot.app.middlewares import setup_middlewares
import os
import django

os.environ["DJANGO_SETTINGS_MODULE"] = "django_core.settings"

django.setup()


async def on_startup() -> None:
    from tgbot_admin.bot.app.others.commands import set_default_commands

    await set_default_commands()
    logger.info("~ Bot startup")


async def on_shutdown() -> None:
    logger.info("~ Bot shutting down...")


async def runbot():
    setup_middlewares(dp)
    setup_handlers(dp)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    await bot(DeleteWebhook(drop_pending_updates=SKIP_UPDATES))
    await dp.start_polling(bot)
