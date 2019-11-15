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

class BaseApi:

    proxies = {
        'http': 'http://192.168.1.105:8888',
        'https': 'http://192.168.1.105:8888'
    }