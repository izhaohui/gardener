#! /usr/bin/env python
# coding:UTF8
# author :zhaohui mail:zhaohui-sol@foxmail.com

import sys

from common import ValveHelper
from common import WxHelper

reload(sys).setdefaultencoding('utf8')
import time
from flask import Flask,make_response,request
import hashlib,logging,sys,xmltodict

URL_PREFIX = "/center"
app = Flask(__name__)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(module)s.%(funcName)s Line:%(lineno)d %(message)s',
    stream=sys.stdout
)


@app.route(URL_PREFIX + '/')
def index():
    return 'it\'s the service center!'

@app.route(URL_PREFIX + '/weixin/check',methods=['GET', 'POST'])
def weixin():
    token = "token"
    openid = request.args.get("openid")
    signature = request.args.get("signature")
    timestamp = request.args.get("timestamp")
    nonce = request.args.get("nonce")
    echostr = request.args.get("echostr")

    args = [token, timestamp, nonce]
    args.sort()

    param_string = "".join(args)
    if hashlib.sha1(param_string).hexdigest() == signature:
        if echostr is not None:
            return echostr
        else:
            params = xmltodict.parse(request.data).get("xml")
            if "Content" in params:
                resp_raw = None
                content = params["Content"]
                if content.isdigit():
                    seconds = int(content) if 10 >= int(content) >= 0 else 2
                    ValveHelper.valve(seconds)
                    resp_raw = WxHelper.reply_text(openid,u"好的，我要浇水喽~")
                else:
                    status = ValveHelper.draw_status()
                    if status:
                        resp_raw = WxHelper.reply_news(openid,[status])
                    else:
                        resp_raw = WxHelper.reply_text(openid,u"老子出错了！")
                logging.warning(resp_raw)
                return resp_raw
            else:
                return "error"
    else:
        return "error"






if __name__ == '__main__':
    app.run()
