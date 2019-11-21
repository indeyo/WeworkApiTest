#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
@Project : WeworkApiTest
@File    : wework.py
@Time    : 2019-11-08  07:31:50
@Author  : indeyo_lin
@Version : 
@Remark  :
"""

from requests import request

class WeWork:

    corpid = 'ww84f2624b18176321'
    contact_secret = '-tzpw8mha37Q7pDSfu22XbLg9EQ38Kx9Dr9aBsX94VU'   # 通讯录的secret
    eat_secret = 'W1a-_z8wERVJRacyrzhuf5W4vHqBTkd2ghvTwAfivwI'   # 吃点啥应用
    contact_token = None
    eat_token = None

    @classmethod
    def get_contact_token(cls):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        param = {'corpid': cls.corpid, 'corpsecret': cls.contact_secret}
        if cls.contact_token == None:
            resp = request('GET', url, params=param).json()
            # print(resp)
            cls.contact_token = resp['access_token']
        return cls.contact_token

    @classmethod
    def get_eat_token(cls):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        param = {'corpid': cls.corpid, 'corpsecret': cls.eat_secret}
        if cls.eat_token == None:
            resp = request('GET', url, params=param).json()
            # print(resp)
            cls.eat_token = resp['access_token']
        return cls.eat_token
