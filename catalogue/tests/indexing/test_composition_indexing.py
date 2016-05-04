from django.conf import settings
from django.test import override_settings
from rest_framework.test import APITestCase
from model_mommy import mommy
import pysolr


class TestCompositionIndexing(APITestCase):

    @override_settings(SOLR={'SERVER': 'http://localhost:8983/solr/test_catalogue'})
    def setUp(self):
        self.server = pysolr.Solr(settings.SOLR['SERVER'])

    def test_solr_index_on_create(self):
        composition = mommy.make("catalogue.Composition", _fill_optional=['title'])
        q = self.server.search("*.*", fq=['type:composition', 'pk:{0}'.format(composition.pk)])
        self.assertTrue(q.hits > 0)

    def test_solr_delete_on_delete(self):
        composition = mommy.make("catalogue.Composition", _fill_optional=['title'])
        composition_pk = composition.pk
        params = {
            'fq': ['type:composition', 'pk:{0}'.format(composition_pk)]
        }
        q = self.server.search("*.*", **params)
        self.assertTrue(q.hits > 0)

        composition.delete()
        q = self.server.search("*.*", **params)
        self.assertTrue(q.hits == 0)

    def test_solr_index_on_update(self):
        composition = mommy.make("catalogue.Composition", _fill_optional=['title'])
        composition_pk = composition.pk
        fq = ['type:composition', 'pk:{0}'.format(composition_pk)]

        new_name = "New Name"
        self.assertFalse((composition.title, new_name))

        composition.name = new_name
        composition.save()
        q = self.server.search('*.*', fq=fq)
        self.assertTrue(q.docs[0]['title_s' == new_name])

    def tearDown(self):
        self.server.delete(q='*:*')
