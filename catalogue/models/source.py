from django.db import models


class Source(models.Model):
    class Meta:
        app_label = "catalogue"

    shelfmark = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.IntegerField(blank=True, null=True)
    end_date = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=127)
    surface = models.CharField(max_length=127)
    type = models.CharField(max_length=127, blank=True, null=True)
    surface = models.CharField(max_length=127, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    archive = models.ForeignKey("catalogue.Archive", blank=True, null=True)

    def __str__(self):
        return "{0}".format(self.shelfmark)
