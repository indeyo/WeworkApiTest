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

from api.base_api import BaseApi

class WeWork(BaseApi):

    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    corpid = 'ww84f2624b18176321'
    contact_secret = '-tzpw8mha37Q7pDSfu22XbLg9EQ38Kx9Dr9aBsX94VU'   # 通讯录的secret
    eat_secret = 'W1a-_z8wERVJRacyrzhuf5W4vHqBTkd2ghvTwAfivwI'   # 吃点啥应用
    contact_token = None
    eat_token = None

    def get_token(self, secret, token):
        param = {'corpid': self.corpid, 'corpsecret': secret}
        if token == None:
            resp = super().request_api(self, 'GET', self.url, params=param).json()
            token = resp['access_token']
        return token

    @classmethod
    def get_contact_token(cls):
        return cls.get_token(cls, cls.contact_secret, cls.contact_token)

    @classmethod
    def get_eat_token(cls):
        return cls.get_token(cls, cls.eat_secret, cls.eat_token)
