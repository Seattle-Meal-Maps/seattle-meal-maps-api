# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 07:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(choices=[(1, 'ALL'), (2, 'Monday'), (3, 'Tuesday'), (4, 'Wednesday'), (5, 'Thursday'), (6, 'Friday'), (7, 'Saturday'), (8, 'Sunday')], unique=True)),
                ('from_hour', models.TimeField(default=None)),
                ('to_hour', models.TimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('address', models.CharField(blank=True, max_length=1000)),
                ('program_type', models.CharField(choices=[('food bank', 'Food Bank'), ('meal program', 'Meal Program')], max_length=255)),
                ('requirements', models.CharField(choices=[('all', 'OPEN TO ALL'), ('women 18+', 'WOMEN 18 AND OLDER'), ('American Indians', 'AMERICAN INDIANS ONLY'), ('55+', 'OPEN TO 55+'), ('men 55+', 'OPEN TO MEN 55+'), ('women and children', 'WOMEN AND CHILDREN ONLY'), ('22 and younger', 'YOUTH 22 AND YOUNGER'), ('60+', 'OPEN TO AGES 60+')], default='OPEN TO ALL', max_length=255)),
                ('meal', models.CharField(choices=[('N/A', 'N/A'), ('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Snack', 'Snack')], default='N/A', max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='servicehours',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hours', to='locations_model.ServiceLocation'),
        ),
    ]
