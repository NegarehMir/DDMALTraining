from django.conf import settings
from django.test import override_settings
from rest_framework.test import APITestCase
from model_mommy import mommy
import pysolr


class TestArchiveIndexing(APITestCase):

    @override_settings(SOLR={'SERVER': 'http://localhost:8983/solr/test_catalogue'})
    def setUp(self):
        self.server = pysolr.Solr(settings.SOLR['SERVER'])

    def test_solr_index_on_create(self):
        archive = mommy.make("catalogue.Archive", _fill_optional=['name'])
        q = self.server.search("*.*", fq=['type:archive', 'pk:{0}'.format(archive.pk)])
        self.assertTrue(q.hits > 0)

    def test_solr_delete_on_delete(self):
        archive = mommy.make("catalogue.Archive", _fill_optional=['name'])
        archive_pk = archive.pk
        params = {
            'fq': ['type:archive', 'pk:{0}'.format(archive_pk)]
        }
        q = self.server.search("*.*", **params)
        self.assertTrue(q.hits > 0)

        source.delete()
        q = self.server.search("*.*", **params)
        self.assertTrue(q.hits == 0)

    def test_solr_index_on_update(self):
        archive = mommy.make("catalogue.Archive", _fill_optional=['name'])
        archive_pk = archive.pk
        fq = ['type:archive', 'pk:{0}'.format(archive_pk)]

        new_name = "New Name"
        self.assertFalse((archive.name, new_name))

        archive.name = new_name
        archive.save()
        q = self.server.search('*.*', fq=fq)
        self.assertTrue(q.docs[0]['name_s' == new_name])

    def tearDown(self):
        # super(TestArchiveIndexing, self).tearDown()
        self.server.delete(q='*:*')
