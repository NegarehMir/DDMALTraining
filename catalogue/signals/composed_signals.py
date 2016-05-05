from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from catalogue.models.composed import Composed


@receiver(post_save, sender=Composed)
def index_composed(sender, instance, created, **kwargs):
    print('Composed saved')


@receiver(post_delete, sender=Composed)
def delete_composed(sender, instance, **kwargs):
    print('Composed deleted')
