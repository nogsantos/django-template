from django.test import TestCase

from core import serializers


class HealthCheckSerializerTest(TestCase):
    def test_serialized_fields(self):
        """Should get default violation serialized fields"""

        serializer = serializers.HealthCheckSerializer()
        serializer_fields = serializer.fields.fields.keys()

        expected_fields = ["response"]

        self.assertEqual(set(serializer_fields), set(expected_fields))
