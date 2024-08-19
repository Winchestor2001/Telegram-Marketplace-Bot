from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton, WebAppInfo
from src.settings import settings


async def start_menu_btn():
    btn = ReplyKeyboardBuilder()
    btn.add(
        KeyboardButton(text='Market', web_app=WebAppInfo(url=settings.bot.WEBAPP_URL))
    )
    return btn.as_markup(resize_keyboard=True)


