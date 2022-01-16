import logging

from nameko.events import EventDispatcher, event_handler, SINGLETON
from nameko.rpc import rpc, RpcProxy
from nameko_sentry import SentryReporter

from services.providers import DjangoModels


class SampleService:
    name = "{{ cookiecutter.project_slug }}_service"

    dispatch = EventDispatcher()
    sentry = SentryReporter()
    models = DjangoModels()
    sampleservice = RpcProxy("{{ cookiecutter.project_slug }}_services")

    @event_handler(
        "{{ cookiecutter.project_slug }}", "sync.{{ cookiecutter.project_slug }}.v1", handler_type=SINGLETON,
    )
    def {{ cookiecutter.project_slug }}_sync_handler(self, payload):
        """
        Simple {{ cookiecutter.project_slug }} sample handler
        """
        logging.info("Received event handler %s", {len(payload or [])})

    @rpc
    def {{ cookiecutter.project_slug }}_rpc_sample(self, payload):
        """
        Simple sample rpc call
        """
        logging.info("Received rpc call %s", {len(payload or [])})
