from rest_framework import viewsets
from api.serializers import LocationSerializer, InfoSerializer
from locations_model.models import ServiceLocation, ServiceInfo
# Create your views here.

class LocationViewSet(viewsets.ReadOnlyModelViewSet):
    """
        API endpoint that allows Food Bank and Meal Program data to be viewed.
    """
    queryset = ServiceLocation.objects.all()
    serializer_class = LocationSerializer

class InfoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ServiceInfo.objects.all()
    serializer_class = InfoSerializer
