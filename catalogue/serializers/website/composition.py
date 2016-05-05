from rest_framework import serializers
from catalogue.models.composition import Composition


class CompositionSerializer(serializers.HyperlinkedModeSerializer):
    class Meta:
        model = Composition
