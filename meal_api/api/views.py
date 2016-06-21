from rest_framework import viewsets
from api.serializers import ServiceSerializer, InfoSerializer
from locations_model.models import ServiceLocation, ServiceInfo
# Create your views here.

class DataViewSet(viewsets.ReadOnlyModelViewSet):
    """
        API endpoint that allows Food Bank and Meal Program data to be viewed.
    """
    queryset = ServiceLocation.objects.all()
    serializer_class = ServiceSerializer

class HoursViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ServiceInfo.objects.all()
    serializer_class = InfoSerializer
