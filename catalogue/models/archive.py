from django.db import models


class Archive(models.model):
    class Meta:
        app_label = "catalogue"

    name = models.CharField(max_length=255)
    city = models.CharField(max_length=127)
    siglum = models.CharField(max_length=127)
    country = models.CharField(max_length=127)