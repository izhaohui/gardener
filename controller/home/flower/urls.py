#!/usr/bin/env python
# coding:UTF8
# author:zhaohui mail:zhaohui-sol@foxmail.com

from django.conf.urls import patterns, url
from views import valve,realtime
urlpatterns = patterns("",
    url(r"^valve$", valve),
    url(r"^realtime$", realtime),
)