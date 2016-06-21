from django.contrib import admin

from .models import ServiceLocation, ServiceInfo

admin.site.register(ServiceLocation)
admin.site.register(ServiceInfo)
