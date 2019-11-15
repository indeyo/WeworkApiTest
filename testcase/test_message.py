#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
@Project : WeworkApiTest
@File    : test_message.py
@Time    : 2019-11-12  07:52:26
@Author  : indeyo_lin
@Version : 
@Remark  :
"""

from api.message import Message

class TestMessage:

    def test_send_message(self):
        msg = Message()
        repr = msg.send_text_massage()
        assert repr['errcode'] == 0