from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from django.db.models import signals
from catalogue.signals.composed_signals import index_composed
from catalogue.models.composed import Composed
from model_mommy import mommy


class ComposedViewTest(APITestCase):
    def setUp(self):
        signals.post_save.disconnect(index_composed, sender=Composed)
        self.composed = mommy.make("catalogue.Composed")
        self.composed.composition = mommy.make("catalogue.Composition")
        self.composed.composer = mommy.make("catalogue.Composer")
        self.composed.save()

    def test_fetches_html_detail_with_success(self):
        # grabs /composed/{pk}
        url = reverse("composed-detail", kwargs={"pk": self.composed.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_fetches_html_detail_with_failure(self):
        url = reverse('composed-detail', kwargs={"pk": 123456789})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def tearDown(self):
        pass
0