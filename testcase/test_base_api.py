#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
@Project : WeworkApiTest
@File    : test_base_api.py
@Time    : 2019-11-25  08:09:28
@Author  : indeyo_lin
@Version : 
@Remark  :
"""
from api.base_api import BaseApi


class TestBaseApi:
    base_api = BaseApi()

    def test_request_api_get(self):
        resp = self.base_api.request_api('GET', 'http://www.baidu.com')
        # assert resp.status_code == 200

    def test_json_format(self):
        json = {"a" : 3, "b" : 4}
        self.base_api.json_format(json)
