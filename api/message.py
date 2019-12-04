#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
@Project : WeworkApiTest
@File    : message.py
@Time    : 2019-11-13  08:32:10
@Author  : indeyo_lin
@Version : 
@Remark  :
"""
from api.wework import WeWork
from api.base_api import BaseApi

import logging

logging.basicConfig(level=logging.INFO)

class Message(BaseApi):

    send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send'
    headers = {'content-type': 'application/json; charset=utf-8'}
    param = {'access_token': WeWork.get_eat_token()}

    def send_text_massage(self):
        json = {
                 "touser": "|".join(['LinXiaoLing']),
                 "msgtype": "text",
                 "agentid": 1000005,
                 "text": {
                     "content": "中午不知道吃啥，吃点啥帮你决定叭！"
                         }
                 }
        resp = super().request_api('POST', self.send_url, json=json, headers=self.headers, params=self.param).json()
        super().json_format(resp)
        return resp