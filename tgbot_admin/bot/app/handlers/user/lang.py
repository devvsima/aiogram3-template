from aiogram import F, types
from aiogram.filters import Command
from aiogram.filters.state import StateFilter

from tgbot_admin.bot.app.routers import user_router as router

from tgbot_admin.services import change_language

from tgbot_admin.bot.app.handlers.msg_text import msg_text
from tgbot_admin.bot.app.keyboards.inline.lang import lang_ikb


@router.message(Command("language"), StateFilter(None))
@router.message(Command("lang"), StateFilter(None))
async def _lang(message: types.Message) -> None:
    """Предлагает клавиатуру с доступными языками"""
    await message.answer(msg_text.CHANGE_LANG, reply_markup=lang_ikb())


@router.callback_query(F.data.in_(["ru", "uk", "en"]))
async def _lang_change(callback: types.CallbackQuery) -> None:
    """Меняет язык пользователя на выбранный"""
    await change_language(callback.from_user.id, callback.data)
    await callback.message.edit_text(msg_text.DONE_CHANGE_LANG)
