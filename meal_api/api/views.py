from rest_framework import viewsets
from api.serializers import ServiceSerializer, HourSerializer
from locations_model.models import ServiceLocation, ServiceHours
# Create your views here.

class DataViewSet(viewsets.ReadOnlyModelViewSet):
    """
        API endpoint that allows Food Bank and Meal Program data to be viewed.
    """
    queryset = ServiceLocation.objects.all()
    serializer_class = ServiceSerializer

class HoursViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ServiceHours.objects.all()
    serializer_class = HourSerializer
