#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
@Project : WeworkApiTest
@File    : base_api.py
@Time    : 2019-11-15  07:45:05
@Author  : indeyo_lin
@Version : 
@Remark  :
"""

from requests import request
import logging

logging.basicConfig(level=logging.INFO)

class BaseApi:

    proxies = {
        'http': 'http://192.168.1.105:8888',
        'https': 'http://192.168.1.105:8888'
    }

    def request_api(self, method, url, param=None, json=None, headers=None, verify=False):
        resp = request(method, url, params=param, json=json, headers=headers, verify=verify).json()
        logging.info("接口返回 %s" % resp)
        return  resp