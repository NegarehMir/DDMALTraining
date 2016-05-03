from django.db import models


class Composer(models.model):
    class Meta:
        app_label = "catalogue"

    name = models.CharField(max_length=255)
