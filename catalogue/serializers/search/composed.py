from rest_framework import serializers
from catalogue.models.composed import Composed


class ComposedSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Composed
        fields = ('pk', 'type', 'certain_b')

    type = serializers.SerializerMethodField()
    pk = serializers.ReadOnlyField()

    certain_b = serializers.ReadOnlyField(source="certain")

    def get_type(self, obj):
        return self.Meta.model.__name__.lower()
