# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

LOCATION_TYPE = [('food bank', 'Food Bank'), ('meal program', 'Meal Program')]
SERVICE_REQUIREMENTS = [
    ('all', 'OPEN TO ALL'),
    ('women 18+', 'WOMEN 18 AND OLDER'),
    ('American Indians', 'AMERICAN INDIANS ONLY'),
    ('55+', 'OPEN TO 55+'),
    ('men 55+', 'OPEN TO MEN 55+'),
    ('women and children', 'WOMEN AND CHILDREN ONLY'),
    ('22 and younger', 'YOUTH 22 AND YOUNGER'),
    ('60+', 'OPEN TO AGES 60+'), ]

MEAL_TYPE = [
    ('N/A', 'N/A'),
    ('Breakfast', 'Breakfast'),
    ('Lunch', 'Lunch'),
    ('Dinner', 'Dinner'),
    ('Snack', 'Snack')]

DAY = [
    ('EVERYDAY', 'EVERYDAY'),
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
]

@python_2_unicode_compatible
class ServiceLocation(models.Model):
    """Model for Food Bank and Meal Programs."""
    name = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=1000, blank=True)
    latitude = models.CharField(max_length=255, blank=True)
    longitude = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class ServiceInfo(models.Model):
    location = models.ForeignKey(ServiceLocation, related_name='program-info')
    program_type = models.CharField(
        max_length=255,
        choices=LOCATION_TYPE
    )
    meal = models.CharField(
        max_length=255,
        choices=MEAL_TYPE,
        default='N/A'
    )
    requirements = models.CharField(
        max_length=255,
        choices=SERVICE_REQUIREMENTS,
        default='OPEN TO ALL'
    )
    day = models.CharField(
        max_length=255,
        choices=DAY,
        default=None
    )
    from_hour = models.TimeField(default=None)
    to_hour = models.TimeField(default=None)

    def __str__(self):
        return str(self.location)
