from build_bot import bot, dp, scheduler
from routers import new_members_router, poll_router, activity_router
from moderate import ban_inactive_members


if __name__ == '__main__':
    scheduler.add_job(ban_inactive_members, 'interval', weeks=4)
    scheduler.start()
    dp.include_routers(new_members_router, poll_router, activity_router)
    dp.run_polling(bot)
