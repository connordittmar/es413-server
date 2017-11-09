# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-07 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('console', '0002_auto_20171106_0839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='obstacle',
            name='position',
        ),
        migrations.RemoveField(
            model_name='telemetry',
            name='position',
        ),
        migrations.RemoveField(
            model_name='waypoint',
            name='position',
        ),
        migrations.AddField(
            model_name='obstacle',
            name='pos_x',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='obstacle',
            name='pos_y',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='telemetry',
            name='pos_x',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='telemetry',
            name='pos_y',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='waypoint',
            name='pos_x',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='waypoint',
            name='pos_y',
            field=models.FloatField(default=0),
        ),
    ]