'''
This Source Code Form is subject to the terms of the Mozilla
Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
'''

# Роутер на активность участников.

from aiogram import Router
from aiogram.types import Message, PollAnswer

activity_router = Router()


def write_down_activity(member_id):
    with open('active_members.txt', 'a') as f:
        f.write(str(member_id) + '\n')


@activity_router.poll_answer()
async def poll_answer_activity_process(poll_answer: PollAnswer):
    write_down_activity(poll_answer.user.id)


@activity_router.message()
async def message_activity_process(message: Message):
    write_down_activity(message.from_user.id)
    print(message.chat.id)
