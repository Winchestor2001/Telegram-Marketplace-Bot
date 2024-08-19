from aiogram import types, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
import logging

from src.apps.profile.crud import create_user_obj
from src.bot.keyboards import start_menu_btn

router = Router()
logger = logging.getLogger(__name__)


@router.message(Command('start'))
async def start_handler(message: types.Message, state: FSMContext):
    await create_user_obj(
        username=message.from_user.username,
        telegram_id=message.from_user.id
    )
    btn = await start_menu_btn()
    await message.answer(text="Assalomu aleykum, Telegram marketplacega qush kelibsiz", reply_markup=btn)
    await state.clear()



