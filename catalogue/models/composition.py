from django.db import models


class Composition(models.Model):
    class Meta:
        app_label = "catalogue"

    title = models.CharField(max_length=255)
    anonymous = models.BooleanField(default=False)
    source = models.ForeignKey("catalogue.Source")
    composer = models.ForeignKey("catalogue.Composer", blank=True, null=True)