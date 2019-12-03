#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
@Project : WeworkApiTest
@File    : Utils.py
@Time    : 2019-11-29  07:48:22
@Author  : indeyo_lin
@Version : 
@Remark  :
"""

import json

class Utils:

    @classmethod
    def format(cls, json_data):
        return json.dumps(json_data, indent=4)