from django.contrib import admin
from catalogue.models.composed import Composed


@admin.register(Composed)
class ComposedAdmin(admin.ModelAdmin):
    pass
