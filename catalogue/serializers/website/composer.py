from rest_framework import serializers
from catalogue.models.composer import Composer


class ComposerSerializer(serializers.HyperlinkedModeSerializer):
    class Meta:
        model = Composer
