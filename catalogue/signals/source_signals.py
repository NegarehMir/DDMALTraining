from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from catalogue.models.source import Source
from catalogue.helpers.solr_helpers import solr_index, solr_delete
from catalogue.serializers.search.source import SourceSearchSerializer

@receiver(post_save, sender=Source)
def index_source(sender, instance, created, **kwargs):
    print('Source saved')


@receiver(post_delete, sender=Source)
def delete_source(sender, instance, **kwargs):
    print('Source deleted')
