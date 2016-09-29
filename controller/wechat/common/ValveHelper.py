#!/usr/bin/env python
# coding:UTF8
# author : zhaohui mail:zhaohui-sol@foxmail.com
import requests

from common import DrawHelper


def valve(seconds = 2):
    response = requests.get("http://192.168.110.11/flower/valve?seconds=" + str(seconds))
    return True if response.content == "OK" else False

def status():
    response = requests.get("http://192.168.110.11/flower/realtime")
    if response.ok:
        json = response.json()
        return json
    else:
        return {}

def draw_status():
    resp = status()
    if resp:
        title = u"小植物好萌哒"
        description = u"当前环境温度 %d 摄氏度，相对湿度 %d%%，土壤湿度 %d%%，今天累计浇水 %d 秒，累计浇水 %dML，好棒哦～" % (resp['env_temperature'],resp['env_humid'],resp['soi_humid'],resp['total_valve_seconds_today'],resp['total_valve_ml_today'])
        text = "%d ML / %d%%" % (resp['total_valve_ml_today'],resp['soi_humid'])
        pic_path = DrawHelper.draw_text("/data/webapps/isol-center/static/image/flower.png",text,36,position=(80,60))
        url = pic_path.replace("/data/webapps/isol-center/","https://isol.me/center/")
        return {
            "Title":title,
            "Description":description,
            "PicUrl":url
        }
    else:
        return {}
