from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class HealthCheckViewTest(TestCase):
    def setUp(self):
        self.host = "core"

    def test_get_request_success(self):
        """Should successfully respond when is on the happy path"""

        response = self.client.get(reverse(f"{self.host}-list"), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
