'''
This Source Code Form is subject to the terms of the Mozilla
Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.
'''

from build_bot import bot, dp, scheduler
from routers import new_members_router, poll_router, activity_router
from moderate import ban_inactive_members


if __name__ == '__main__':
    scheduler.add_job(ban_inactive_members, 'interval', weeks=4)
    scheduler.start()
    dp.include_routers(new_members_router, poll_router, activity_router)
    dp.run_polling(bot)
