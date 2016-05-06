from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from django.db.models import signals
from catalogue.signals.source_signals import index_source
from catalogue.models.source import Source
from model_mommy import mommy
from django.test import Client
import json

class SourceViewTest(APITestCase):
    def setUp(self):
        signals.post_save.disconnect(index_source, sender=Source)
        self.source = mommy.make("catalogue.Source")

    def test_fetches_html_detail_with_success(self):
        # grabs /source/{pk}
        url = reverse("source-detail", kwargs={"pk": self.source.pk})
        response = self.client.get(url)
        c = Client(HTTP_ACCEPT='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_fetches_html_detail_with_failure(self):
        url = reverse('source-detail', kwargs={"pk": 123456789})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_fetches_json_detail_with_success(self):
        url = reverse("source-detail", kwargs={"pk": self.source.pk})
        response = self.client.get(url, HTTP_ACCEPT='application/json')
        print(response["content-type"])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_fetches_json_detail_with_failure(self):
        url = reverse('source-detail', kwargs={"pk": 123456789})
        response = self.client.get(url, HTTP_ACCEPT='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def tearDown(self):
        pass
