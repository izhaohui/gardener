#!/usr/bin/env python
# coding:UTF8
# author:zhaohui mail:zhaohui-sol@foxmail.com

import sys
import socket
import logging
from flower.models import Sensor
from django_cron import CronJobBase, Schedule

reload(sys).setdefaultencoding('utf8')


class SensorFetcher(CronJobBase):
    RUN_EVERY_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'home.flower.sensorfetcher'

    def do(self):
        Sensor.valve(0)
