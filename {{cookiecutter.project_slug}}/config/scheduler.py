import logging
import schedule
import time

from datetime import datetime
from decouple import config
{% if cookiecutter.use_nameko == "y" -%}
from nameko.standalone.events import event_dispatcher
from nameko.standalone.rpc import ClusterRpcProxy
{%- endif %}

class AppScheduler:
    """
    Schedule docs definition at:
    https://schedule.readthedocs.io/en/stable/examples.html#run-a-job-every-x-minute
    """
    RUNNING = config('RUNNING', default=True, cast=bool)
    PRODUCTION_ENV = config('PRODUCTION_ENV', default=False, cast=bool)
    {% if cookiecutter.use_nameko == "y" -%}
    RABBITMQ_HOST = config('RABBITMQ_HOST', default="localhost")
    RABBITMQ_USER = config('RABBITMQ_USER', default="guest")
    RABBITMQ_PASSWORD = config('RABBITMQ_PASSWORD', default="guest")

    CONFIG = {
        "AMQP_URI": f"amqp://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}"
    }

    def dispatch_event(
        self, event_type, service_name="scheduler_service", event_data=""
    ):
        """
        Dispatch an event
        """
        logging.info(
            "Event %s start - Service %s - Data %s ",
            event_type, service_name, event_data
        )


        dispatch = event_dispatcher(self.CONFIG)
        dispatch(service_name, event_type, event_data)

    def call_async_rpc(self, service_name, task_name):
        """
        RPC Assinc call
        """
        with ClusterRpcProxy(self.CONFIG) as cluster_rpc:
            method = getattr(cluster_rpc[service_name], task_name)
            method.call_async()
    {%- endif %}

    def add_schedules(self):
        """
        Define schedulers

        Ex:
        {%- if cookiecutter.use_nameko == "y" -%}
        # Sync archive contracts every half past hour
        schedule.every().hour.at(":15").do(
            dispatch_event, event_type="service.sync_some_data.v1"
        )
        {%- else %}
        # Run job every hour at the 42rd minute
        schedule.every().hour.at(":42").do(job)
        {%- endif %}

        """
        if self.PRODUCTION_ENV:
            # Replace with scheduler
            ...

    def run(self):
        logging.basicConfig(
            format="%(asctime)s - %(message)s", level=logging.INFO
        )
        logging.info("Schedule started at %s", datetime.now())

        self.add_schedules()

        while self.RUNNING:
            schedule.run_pending()
            time.sleep(1)


if __name__ == "__main__":
    AppScheduler().run()
