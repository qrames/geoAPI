from rest_framework import serializers
from .models import GeoPoint


class GeoPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoPoint

        fields = ('name', 'geom')
