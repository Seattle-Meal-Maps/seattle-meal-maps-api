# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 08:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations_model', '0002_auto_20160614_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicehours',
            name='day',
            field=models.CharField(choices=[('ALL', 'ALL'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default=None, max_length=255),
        ),
    ]
