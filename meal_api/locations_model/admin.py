from django.contrib import admin

from .models import ServiceLocation, ServiceHours

admin.site.register(ServiceLocation)
admin.site.register(ServiceHours)
