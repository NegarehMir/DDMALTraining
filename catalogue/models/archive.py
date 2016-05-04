from django.db import models


class Archive(models.Model):
    class Meta:
        app_label = "catalogue"

    name = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=127, blank=True, null=True)
    siglum = models.CharField(max_length=127)
    country = models.CharField(max_length=127, blank=True, null=True)

    def __str__(self):
        return "{0}".format(self.name)
