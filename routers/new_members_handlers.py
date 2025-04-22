'''
This Source Code Form is subject to the terms of the Mozilla
Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
'''

# Роутер на новых участников.

from aiogram import Router, F
from aiogram.types import Message, ChatJoinRequest, CallbackQuery
from build_bot import bot, rules, accept_keyboard, accept_inline_keyboard, GROUP_ID
import moderate

new_members_router = Router()


@new_members_router.chat_join_request()
async def approve_join_request_process(request: ChatJoinRequest):
    await request.approve()


@new_members_router.message(F.new_chat_member)
async def new_chat_member_process(message: Message):
    for member in message.new_chat_members:
        await moderate.restrict_member(member_id=member.id)
        try:
            await bot.send_message(chat_id=member.id, text=rules, parse_mode='HTML', reply_markup=accept_keyboard)
        except:
            await message.answer(text=f'@{member.username}\n{rules}', parse_mode='HTML', reply_markup=accept_inline_keyboard)


@new_members_router.message(F.text == '✅ Принять')
async def accept_rules_process(message: Message):
    await moderate.expand_member(message.from_user.id)
    await message.answer(text='Вы приняли правила.\n'
                              '✅ Теперь вам доступны сообщения')


@new_members_router.callback_query(F.data == 'accept')
async def accept_rules_callback_process(callback: CallbackQuery):
    if callback.message.text.find('@' + str(callback.from_user.username)) == 0:
        await moderate.expand_member(callback.from_user.id)
        await bot.delete_message(chat_id=GROUP_ID, message_id=callback.message.message_id)
