#!/usr/bin/env python
# coding:UTF8
# author : zhaohui mail:zhaohui-sol@foxmail.com
import os,random
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

FONT = "/data/webapps/isol-center/static/font/YaHei.ttc"
OUTPUT = "/data/webapps/isol-center/static/image"

def draw_text(path,text,size,position = (0,0)):
    if path and text and size and position and os.path.exists(path):
        image = Image.open(path)
        drawer = ImageDraw.Draw(image)
        font = ImageFont.truetype(FONT, size)
        drawer.text(position, text , (255, 255, 255), font=font)
        filename = "%s/%d.png" % (OUTPUT,random.randint(0,100000000000))
        image.save(filename)
        return filename
    else:
        return None


