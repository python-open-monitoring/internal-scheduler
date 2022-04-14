import datetime
import json
from contextlib import asynccontextmanager

import aiormq
from simple_print import sprint

from database import methods as db_methods
from settings import AMQP_URI


@asynccontextmanager
async def rabbitmq_get_channel():
    connection = await aiormq.connect(AMQP_URI)
    try:
        channel = await connection.channel()
        yield channel
    finally:
        await connection.close()


async def internal_monitor__monitor():
    time_now = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    sprint(f"AMQP PRODUCER:     internal_monitor__monitor time={time_now}", с="green", s=1, p=1)
    monitors = await db_methods.select_monitors()
    async with rabbitmq_get_channel() as channel:
        for monitor in monitors:
            outcoming_data_bytes = json.dumps(monitor).encode()
            await channel.basic_publish(outcoming_data_bytes, routing_key=f"monitoring:internal__monitor:monitor")
