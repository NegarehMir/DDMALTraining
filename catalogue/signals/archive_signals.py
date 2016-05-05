from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from catalogue.models.archive import Archive
from catalogue.helpers.solr_helpers import solr_index, solr_delete
from catalogue.serializers.search.archive import ArchiveSearchSerializer


@receiver(post_save, sender=Archive)
def index_archive(sender, instance, created, **kwargs):
    solr_index(ArchiveSearchSerializer, [instance])


@receiver(post_delete, sender=Archive)
def delecte_source(sender, instance, **kwargs):
    solr_delete([instance])
