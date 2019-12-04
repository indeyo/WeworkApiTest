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

from utils.Utils import Utils

logging.basicConfig(level=logging.INFO)

class BaseApi:

    proxies = {
        'http': 'http://192.168.1.105:8888',
        'https': 'http://192.168.1.105:8888'
    }

    def json_format(self, json_data):
        print(Utils.format(json_data))

    def request_api(self, method, url, params=None, json=None, headers=None, verify=False):
        resp = request(method, url, params=params, json=json, headers=headers, verify=verify)
        resp_json = resp.json()
        logging.info("接口返回 %s" % resp.json())
        # self.json_format(resp_json)    #  报错：TypeError: json_format() missing 1 required positional argument: 'json_data'
        return resp