from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import School


class SchoolSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = School
        geo_field = 'location'
        fields = ['name', 'regional', 'level', 'governance']
        read_only_fields = ['location', 'created_at', 'updated_at']
