# Роутер на создание опроса к тренировке.

from aiogram import Router, F
from aiogram.types import Message

from .activity_handlers import write_down_activity

poll_router = Router()


@poll_router.message(F.poll)
async def poll_create_process(message: Message):
    await message.answer_poll(question=message.poll.question,
                              options=[option.text for option in message.poll.options],
                              is_anonymous=False)
    await message.delete()
    write_down_activity(message.from_user.id)
