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
        content = "中午不知道吃啥，吃点啥帮你决定叭！"
        repr = msg.send_text_massage(['LinXiaoLing'], 1000005, content)
        assert repr['errcode'] == 0