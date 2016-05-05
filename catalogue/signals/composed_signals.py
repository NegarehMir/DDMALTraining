from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from catalogue.models.composed import Composed
from catalogue.helpers.solr_helpers import solr_index, solr_delete
from catalogue.serializers.search.composed import ComposedSearchSerializer


@receiver(post_save, sender=Composed)
def index_composed(sender, instance, created, **kwargs):
    solr_index(ComposedSearchSerializer, [instance])


@receiver(post_delete, sender=Composed)
def delete_composed(sender, instance, **kwargs):
    solr_delete([instance])
