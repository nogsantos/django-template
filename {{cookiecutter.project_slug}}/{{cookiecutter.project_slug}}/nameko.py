from django.conf import settings
from nameko.standalone.rpc import ClusterRpcProxy


def make_rpc(service, method, call_async=True, **kwargs):
    """
    Enables to make an RPC call sync or async
    """
    with ClusterRpcProxy(settings.CONFIG_NAMEKO) as cluster_rpc:
        method = getattr(cluster_rpc[service], method)
        if call_async:
            method.call_async(**kwargs)
        else:
            return method(**kwargs)
