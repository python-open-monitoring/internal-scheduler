from starlette.applications import Starlette
from simple_print import sprint
from crontab import monitors


class AmqpHttpServer(Starlette):
    def __init__(self, *args, **kwargs):
        monitors.start()
        sprint("Monitors start", s=1, p=1)
        super().__init__(*args, **kwargs)


app = AmqpHttpServer(debug=True)
