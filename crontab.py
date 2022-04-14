import aiocron

from producer import methods as producer_methods


@aiocron.crontab("*/1 * * * *", start=False)
async def monitors():
    await producer_methods.internal_monitor__monitor()
