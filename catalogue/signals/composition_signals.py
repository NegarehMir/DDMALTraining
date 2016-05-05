from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from catalogue.models.composition import Composition
from catalogue.helpers.solr_helpers import solr_index, solr_delete
from catalogue.serializers.search.composition import CompositionSearchSerializer


@receiver(post_save, sender=Composition)
def index_composition(sender, instance, created, **kwargs):
    solr_index(CompositionSearchSerializer, [instance])


@receiver(post_delete, sender=Composition)
def delete_composition(sender, instance, **kwargs):
    solr_delete([instance])
