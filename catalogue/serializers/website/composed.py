from rest_framework import serializers
from catalogue.models.composed import Composed


class ComposedSerializer(serializers.HyperlinkedModeSerializer):
    class Meta:
        model = Composed
