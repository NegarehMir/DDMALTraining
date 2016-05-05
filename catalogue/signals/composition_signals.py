from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from catalogue.models.composition import Composition


@receiver(post_save, sender=Composition)
def index_composition(sender, instance, created, **kwargs):
    print('Composition saved')


@receiver(post_composition, sender=Composition)
def delecte_source(sender, instance, **kwargs):
    print('Composition deleted')
