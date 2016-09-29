#!/usr/bin/env python
# coding:UTF8
# author : zhaohui mail:zhaohui-sol@foxmail.com
import xmltodict,time


def reply_text(openid,text):
    resp = {
        "xml": {
            "ToUserName": openid,
            "FromUserName": "wechat_username",
            "CreateTime": int(time.time()),
            "MsgType": "text",
            "Content": text
        }
    }
    return xmltodict.unparse(resp)


def reply_news(openid,news = []):
    resp = {
        "xml":{
            "ToUserName": openid,
            "FromUserName": "wechat_username",
            "CreateTime": int(time.time()),
            "MsgType": "news",
            "ArticleCount": len(news),
            "Articles":[]
        }
    }
    for new in news:
        resp.get("xml").get("Articles").append({
            "item":{
                "Title":new['Title'],
                "Description":new["Description"],
                "PicUrl":new["PicUrl"]
            }
        })
    return xmltodict.unparse(resp)



