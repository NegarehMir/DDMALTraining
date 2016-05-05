from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from catalogue.models.archive import Archive


@receiver(post_save, sender=Archive)
def index_archive(sender, instance, created, **kwargs):
    print('Archive saved')


@receiver(post_archive, sender=Archive)
def delecte_source(sender, instance, **kwargs):
    print('Archive deleted')
