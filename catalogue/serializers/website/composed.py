from rest_framework import serializers
from catalogue.models.composed import Composed


class ComposedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Composed
