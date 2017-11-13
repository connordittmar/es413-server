# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from .models import Telemetry, Position, VehicleSettings, Config
# Create your views here.
frommatlab = True
def post_telemetry(request):
    if frommatlab == True:
        try:
            output = json.loads(request.POST.items()[0][0])
            boatid = output['boatid']
            pos_x = float(output['pos_x'])
            pos_y = float(output['pos_y'])
            heading = float(output['heading'])
            timestamp = float(output['timestamp'])
            telemetry = Telemetry(pk=1,
                boatid=boatid,pos_x=pos_x,pos_y=pos_y,heading=heading,timestamp=timestamp)
            telemetry.save()
            return HttpResponse('posted.')
        except Exception as exc:
            print "Exception: ", exc
            return HttpResponse('Error! %s' % exc)

    else:
        try:
            output = request.POST
            pos_x = float(output['pos_x'])
            pos_y = float(output['pos_y'])
            heading = float(output['heading'])
            timestamp = float(output['timestamp'])
            telemetry = Telemetry(
                pk=1,pos_x=pos_x,pos_y=pos_y,heading=heading,timestamp=timestamp)
            telemetry.save()
            return HttpResponse('posted.')
        except Exception as exc:
            print "Exception: ", exc
            return HttpResponse('Error! %s' % exc)

def get_telemetry(request):
    telemetry = Telemetry.objects.get(pk=1) #this returns the first telemetry object it finds
    nmea_string = '$,%s,%.3f,%7.3f,%7.3f,%5.1f,!' % (telemetry.boatid,telemetry.timestamp,telemetry.pos_x,telemetry.pos_y,telemetry.heading)
    return HttpResponse(nmea_string)


def console_home(request):
    telem_list = Telemetry.objects.order_by('-id')
    context = {'telem_list': telem_list}
    return render(request, 'console/index.html',context)

def handle_settings(request):
    settings = get_object_or_404(VehicleSettings)
    if request.method == 'POST':
        setattr(settings, request.POST['setting'])
        settings.save()
        return HttpResponseRedirect((''))
    else:
        context = {'settings': settings}
        return render(request,'console/settings.html')

def hook_telemetry(request):
    telemetry = serializers.serialize("json",[Telemetry.objects.get(pk=1)]) #this returns the first telemetry object it finds
    return HttpResponse(telemetry)
