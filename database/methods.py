import pprint

import asyncpg

from settings import DATABASE_URI


async def select_monitors(test=False):

    conn = await asyncpg.connect(DATABASE_URI)

    monitor_records = f"""  
    SELECT *
    FROM "monitoring_monitor" 
    WHERE "monitoring_monitor"."active" = TRUE;
    """

    try:
        monitor_records = await conn.fetch(monitor_records)
    except:
        monitor_records = []
    finally:
        await conn.close()

    response = []
    for monitor_record in monitor_records:
        monitor_records_dict = {}
        monitor_records_dict["monitor_id"] = str(monitor_record["id"])
        monitor_records_dict["monitor_name"] = str(monitor_record["name"])
        monitor_records_dict["monitor_host"] = str(monitor_record["host"])
        monitor_records_dict["monitor_port"] = str(monitor_record["port"])
        response.append(monitor_records_dict)

    if test:
        pprint.pprint(response)

    return response
