from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from catalogue.models.composer import Composer


@receiver(post_save, sender=Composer)
def index_composer(sender, instance, created, **kwargs):
    print('Composer saved')


@receiver(post_delete, sender=Composer)
def delete_composer(sender, instance, **kwargs):
    print('Composer deleted')
