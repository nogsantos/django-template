from rest_framework import serializers


class HealthCheckSerializer(serializers.Serializer):
    response = serializers.CharField(
        max_length=2,
        help_text="Response health check field",
        required=False,
        read_only=True,
        default="OK",
    )
