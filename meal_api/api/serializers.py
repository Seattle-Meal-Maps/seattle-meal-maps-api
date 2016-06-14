from rest_framework import serializers
from locations_model.models import ServiceLocation, ServiceHours

class HourSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceHours
        fields = ('day', 'from_hour', 'to_hour')

class ServiceSerializer(serializers.ModelSerializer):
    hours = HourSerializer(many=True, read_only=True)

    class Meta:
        model = ServiceLocation
        fields = ('name', 'address', 'program_type', 'requirements', 'meal', 'hours')
