# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Position, Obstacle, Telemetry, VehicleState, Config
# Register your models here.

admin.site.register(Position)
admin.site.register(Obstacle)
admin.site.register(Telemetry)
admin.site.register(VehicleState)
admin.site.register(Config)