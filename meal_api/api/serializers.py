from rest_framework import serializers
from locations_model.models import ServiceLocation, ServiceInfo

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceInfo
        fields = ('program_type', 'requirements', 'meal', 'day', 'from_hour', 'to_hour')

class LocationSerializer(serializers.ModelSerializer):
    data = InfoSerializer(many=True, read_only=True)

    class Meta:
        model = ServiceLocation
        fields = ('name', 'address', 'latitude', 'longitude', 'data')
