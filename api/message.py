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
from requests import request
from api.wework import WeWork
from api.base_api import BaseApi

import logging

logging.basicConfig(level=logging.INFO)

class Message(BaseApi):

    def send_text_massage(self):

        url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send'
        # headers = {'content-type': 'application/json; charset=utf-8'}
        headers = {'content-type': 'charset=utf-8'}
        param = {'access_token': WeWork.get_eat_token()}
        json = {
                 "touser": "|".join(['LinXiaoLing']),
                 "msgtype": "text",
                 "agentid": 1000005,
                 "text": {
                     "content": "中午不知道吃啥，吃点啥帮你决定叭！"
                         }
                 }
        # repr = post(url, json=json, headers=headers, params=param, verify=False, proxies=proxies).json()
        resp = request('POST', url, json=json, headers=headers, params=param, verify=False).json()
        logging.info('发送消息接口返回：%s' % resp)
        return resp