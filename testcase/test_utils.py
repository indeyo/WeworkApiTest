#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
@Project : WeworkApiTest
@File    : test_utils.py
@Time    : 2019-11-29  07:59:33
@Author  : indeyo_lin
@Version : 
@Remark  :
"""
from utils.Utils import Utils


class TestUtils:

    def test_format(self):
        jsondata = {"a" : 3, "b" : 4}
        print(Utils.format(jsondata))