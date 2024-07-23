from build_bot import bot
from aiogram.types import ChatPermissions
from build_bot import GROUP_ID #, userbot


async def ban_inactive_members():
    # with open('active_members.txt', 'r') as f:
    #     activity = f.readlines()
    # activity = list(set([id.replace('\n', '') for id in activity]))
    # print(activity)
    #
    # with usebot.start():
    #     all_members = [member.id for member in userbot.get_participants(GROUP_ID)]
    #
    # for member_id in all_members:
    #     if member_id not in activity:
    #         try:
    #             await bot.ban_chat_member(chat_id=GROUP_ID, member_id=member_id)
    #         finally:
    #             pass
    # f = open('active_members.txt', 'w')
    # f.close()
    print('Тут должен быть бан')


async def restrict_member(member_id: int):
    await bot.restrict_chat_member(chat_id=GROUP_ID, user_id=member_id,
                                   permissions=ChatPermissions(can_send_messages=False,
                                                               can_send_other_messages=False,
                                                               can_send_audios=False,
                                                               can_send_photos=False,
                                                               can_send_videos=False))


async def expand_member(member_id: int):
    await bot.restrict_chat_member(chat_id=GROUP_ID, user_id=member_id,
                                   permissions=ChatPermissions(can_send_messages=True,
                                                               can_send_other_messages=True,
                                                               can_send_audios=True,
                                                               can_send_photos=True,
                                                               can_send_videos=True))
