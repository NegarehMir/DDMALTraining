from django.db import models


class Composed(models.Model):
    class Meta:
        app_label = "catalogue"

    certain = models.BooleanField(default=True)
    composition = models.ForeignKey("catalogue.Composition", blank=True, null=True)
    composer = models.ForeignKey("catalogue.Composer", blank=True, null=True)

    def __str__(self):
        return "{0}".format(self.certain)