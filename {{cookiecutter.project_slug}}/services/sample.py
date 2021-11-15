import logging

from django.db.models import prefetch_related_objects

from nameko.events import EventDispatcher, event_handler, SINGLETON
from nameko.rpc import rpc, RpcProxy
from nameko_sentry import SentryReporter

from services.providers import DjangoModels


class SampleService:
    name = "sample_service"

    dispatch = EventDispatcher()
    sentry = SentryReporter()
    models = DjangoModels()
    sampleservice = RpcProxy("sampleservice")

    @event_handler(
        "service",
        "sync.sample.v1",
        handler_type=SINGLETON,
    )
    def sample_handler(self, payload):
        """
        Simple sample handler
        """
        logging.info(
            "Received event handler %s", {len(payload or [])}
        )

    @rpc
    def sample_rpc(self, payload):
        """
        Simple sample rpc call
        """
        logging.info("Received rpc call %s", {len(payload or [])})