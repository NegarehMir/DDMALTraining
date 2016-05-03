from django.db import models


class Composition(models.model):
    class Meta:
        app_label = "catalogue"

    title = models.CharField(max_length=255, blank=True, null=True)
    anonymous = models.BooleanField(default=False)