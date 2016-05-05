from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from catalogue.models.composer import Composer
from catalogue.helpers.solr_helpers import solr_index, solr_delete
from catalogue.serializers.search.composer import ComposerSearchSerializer


@receiver(post_save, sender=Composer)
def index_composer(sender, instance, created, **kwargs):
    solr_index(ComposerSearchSerializer, [instance])


@receiver(post_delete, sender=Composer)
def delete_composer(sender, instance, **kwargs):
    solr_delete([instance])
