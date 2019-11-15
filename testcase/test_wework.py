#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
@Project : WeworkApiTest
@File    : test_wework.py
@Time    : 2019-11-08  07:32:56
@Author  : indeyo_lin
@Version : 
@Remark  :
"""

from api.wework import WeWork

class TestWeWork:

    def test_get_contact_token(self):
        assert WeWork.get_contact_token() != None

    def test_get_eat_token(self):
        assert WeWork.get_eat_token() != None