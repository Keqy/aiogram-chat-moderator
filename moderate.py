from build_bot import bot
from aiogram.types import ChatPermissions


async def ban_inactive_members():
    with open('active_members.txt', 'r') as f:
        active_members = f.readlines()
        active_members = list(set(active_members))
    await bot.get_chat_member()


async def restrict_member(group_id: int, member_id: int):
    await bot.restrict_chat_member(chat_id=group_id, user_id=member_id,
                                   permissions=ChatPermissions(can_send_messages=False,
                                                               can_send_other_messages=False,
                                                               can_send_audios=False,
                                                               can_send_photos=False,
                                                               can_send_videos=False))


async def expand_member(group_id: int, member_id: int):
    await bot.restrict_chat_member(chat_id=group_id, user_id=member_id,
                                   permissions=ChatPermissions(can_send_messages=True,
                                                               can_send_other_messages=True,
                                                               can_send_audios=True,
                                                               can_send_photos=True,
                                                               can_send_videos=True))