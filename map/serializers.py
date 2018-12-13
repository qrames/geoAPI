from rest_framework import serializers
from .models import GeoPoint

from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometrySerializerMethodField

class GeoPointSerializer(GeoFeatureModelSerializer):


    class Meta:
        model = GeoPoint
        geo_field = 'geom'
        fields = ('name', 'geom')
