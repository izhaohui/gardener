#!/usr/bin/env python
# coding:UTF8
# author:zhaohui mail:zhaohui-sol@foxmail.com
import time
import datetime
import logging

from django.db.models import Sum
from django.shortcuts import render,RequestContext,render_to_response
from django.http.response import JsonResponse,Http404,HttpResponse
from models import Sensor
import socket

# Create your views here.

def valve(req):
    status = False
    seconds = req.GET.get("seconds","0")
    try:
        seconds = int(seconds)
        assert 10 >= seconds >= 0
    except:
        seconds = 0
    status = Sensor.valve(seconds)
    return HttpResponse("OK" if status else "ERR")


def realtime(req):
    data = dict()

    try:
        date = datetime.datetime.now().date()
        model = Sensor.objects.latest("timestamp")
        data['timestamp'] = time.mktime(model.timestamp.timetuple()) * 1000
        data['env_light'] = model.env_light
        data['env_humid'] = model.env_humid
        data['env_raindrop'] = model.env_raindrop
        data['env_temperature'] = model.env_temperature
        data['soi_humid'] = (1 - model.soi_humid * 1.0 / 1024) * 100
        data['soi_fatness'] = model.soi_fatness
        data['soi_temperature'] = model.soi_temperature
        data['valve_flow'] = model.valve_flow
        data['valve_span'] = model.valve_span
        days_set = Sensor.objects.filter(timestamp__gte = date)
        data['total_valve_seconds_today'] = days_set.aggregate(total = Sum("valve_span"))['total']
        data['total_valve_ml_today'] = data['total_valve_seconds_today'] * 100
    except Exception,e:
        model = None

    return JsonResponse(data)

