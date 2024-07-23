import os
import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telethon import TelegramClient


scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# API_ID: int =
# API_HASH: str = ''
# PHONE: str =
BOT_TOKEN: str = os.getenv('BOT_TOKEN')
GROUP_ID: int = os.getenv('GROUP_ID')
rules: str = """Перед вступлением в группу, ознакомьтесь с правилами чата Хоккейного Клуба О.С.А<b><i>
1. Чат предназначен для общение на хоккейную и околохоккейную тему. Обсуждение сторонних вопросов не приветствуется.\n\n
2. Все занятия клуба проводятся на платной основе. Либо месячный абонемент, либо разовое посещение.\n\n
3. Все участники клуба должны давать обратную связь на вопросы в ветке «Тренировки», даже если ответ отрицательный.\n\n 
4. За отсутствие активности в течении месяца, член клуба удаляется ботом из чата автоматически.</i></b>"""
accept_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='✅ Принять')]],
                                      resize_keyboard=True,
                                      one_time_keyboard=True)
accept_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='✅ Принять',
                                                                                     callback_data='accept')]])
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)
# userbot = TelegramClient(session=PHONE, api_id=API_ID, api_hash=API_HASH)
