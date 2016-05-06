from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from django.db.models import signals
from catalogue.signals.source_signals import index_source
from catalogue.models.source import Source
from model_mommy import mommy
from django.test import Client
from django.conf import settings
import pysolr
import json

class SourceSearchViewTest(APITestCase):
    def setUp(self):
        self.server = pysolr.Solr(settings.SOLR['SERVER'])
        self.source = mommy.make("catalogue.Source")

    def test_indexes_and_is_found_with_pk_search(self):
        # grabs /search/?pk=1
        url = reverse("search-list")
        response = self.client.get(url, { 'format' : 'json', 'pk': self.source.pk })
        c = Client(HTTP_ACCEPT='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.pk, self.source.pk)

    def test_indexes_and_is_not_found_with_pk_search(self):
        # looks for /search/?pk=1 and shouldn't find it
        url = reverse("search-list")
        response = self.client.get(url, { 'format' : 'json', 'pk': '123456789' })


    def test_fetches_json_detail_with_failure(self):
        url = reverse('source-detail', kwargs={"pk": 123456789})
        response = self.client.get(url, HTTP_ACCEPT='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def tearDown(self):
        pass
