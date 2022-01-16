from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.response import Response

from core.serializers import HealthCheckSerializer


class HealthCheckViewSet(viewsets.ViewSet):
    """
    list:
        health check

        Check the service status
    """

    serializer_class = HealthCheckSerializer

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: HealthCheckSerializer()},
        tags=["service"],
    )
    def list(self, request):
        serializer = self.serializer_class({"OK"})
        return Response(serializer.data, status=status.HTTP_200_OK)
