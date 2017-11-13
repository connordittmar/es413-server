# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.forms import ModelForm
from django.db import models
# Create your models here.
class Position(models.Model):
    pos_x = models.FloatField(default = 0)
    pos_y = models.FloatField(default = 0)

class Obstacle(models.Model):
    pos_x = models.FloatField(default = 0)
    pos_y = models.FloatField(default = 0)
    radius = models.FloatField()

class Config(models.Model):
    frommatlab = models.BooleanField(default=True)

class Telemetry(models.Model):
    boatid = models.CharField(max_length = 10, blank = True)
    pos_x = models.FloatField(default = 0)
    pos_y = models.FloatField(default = 0)
    heading = models.FloatField(default = 0)
    timestamp = models.FloatField(default = 0)

class Waypoint(models.Model):
    pos_x = models.FloatField(default = 0)
    pos_y = models.FloatField(default = 0)

class WaypointForm(ModelForm):
    class Meta:
        model = Waypoint
        fields = ['pos_x','pos_y']

class VehicleSettings(models.Model):
    MODE_CHOICES = (
        ('auto','auto'),
        ('guided','guided'),
    )
    mode = models.CharField(
        choices = MODE_CHOICES,
        default = 'auto',
        max_length = 10,
        blank = True,
    )
    armed = models.BooleanField(default=False, blank=True)
    gain_p = models.FloatField(default=1, blank=True)
    gain_speed = models.FloatField(default=1, blank=True)
    waypoint_index = models.IntegerField(default=1, blank=True)

class VehicleState(models.Model):
    telemetry = models.ForeignKey(
        'Telemetry',
        on_delete=models.CASCADE,
    )
    settings = models.ForeignKey(
        'VehicleSettings',
        on_delete=models.CASCADE,
        default = 1
    )
