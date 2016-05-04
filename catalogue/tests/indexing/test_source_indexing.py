from rest_framework.test import APITestCase
from model_mommy import mommy

class TestSourceIndexing(APITestCase):
    def setUp(self):
        pass

    def test_solr_index_on_create(self):
        source = mommy.make("catalogue.Source", _fill_optional=['name'])
        self.assertIsNotNone(source)

    def test_solr_delete_on_delete(self):
        pass

    def test_solr_index_on_update(self):
        pass

    def tearDown(self):
        pass
