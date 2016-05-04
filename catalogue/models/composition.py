from django.db import models


class Composition(models.Model):
    class Meta:
        app_label = "catalogue"

    title = models.CharField(max_length=255)
    anonymous = models.BooleanField(default=False)
    source = models.ForeignKey("catalogue.Source", blank=True, null=True)
    composers = models.ManyToManyField("catalogue.Composer", through='catalogue.Composed')

    def __str__(self):
        return "{0}".format(self.title)
