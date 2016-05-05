from django.conf import settings
from django.test import override_settings
from rest_framework.test import APITestCase
from model_mommy import mommy
import pysolr


@override_settings(SOLR={'SERVER': 'http://localhost:8983/solr/test_catalogue'})
class TestComposedIndexing(APITestCase):

    def setUp(self):
        self.server = pysolr.Solr(settings.SOLR['SERVER'])

    def test_solr_index_on_create(self):
        composed = mommy.make("catalogue.Composed")
        q = self.server.search("*:*", fq=['type:composed', 'pk:{0}'.format(composed.pk)])
        self.assertTrue(q.hits > 0)

    def test_solr_delete_on_delete(self):
        composed = mommy.make("catalogue.Composed")
        composed_pk = composed.pk
        params = {
            'fq': ['type:composed', 'pk:{0}'.format(composed_pk)]
        }
        q = self.server.search("*:*", **params)
        self.assertTrue(q.hits > 0)

        composed.delete()
        q = self.server.search("*:*", **params)
        self.assertTrue(q.hits == 0)

    def test_solr_index_on_update(self):
        composed = mommy.make("catalogue.Composed")
        composed_pk = composed.pk
        fq = ['type:composed', 'pk:{0}'.format(composed_pk)]

        new_certain = not composed.certain

        composed.certain = new_certain
        composed.save()
        q = self.server.search('*:*', fq=fq)
        self.assertTrue(q.docs[0]['certain_b'] == new_certain)

    def tearDown(self):
        self.server.delete(q='*:*')
