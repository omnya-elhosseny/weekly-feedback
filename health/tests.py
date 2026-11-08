from django.test import TestCase
from django.urls import reverse


class HealthCheckTests(TestCase):
    def test_health_page_responds_successfully(self):
        response = self.client.get(reverse("health_check"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"OK")
