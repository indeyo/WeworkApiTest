#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
@Project : WeworkApiTest
@File    : department.py
@Time    : 2019-11-07  08:21:31
@Author  : indeyo_lin
@Version : 
@Remark  :
"""
import time
import calendar
import logging
from requests import request

from api.base_api import BaseApi
from api.wework import WeWork

logging.basicConfig(level=logging.INFO)

class Department(BaseApi):

    def get_department_list(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list'
        param = {'access_token': WeWork.get_contact_token()}
        resp = super().request_api('GET', url, params=param).json()
        return resp

    def create_department(self, depart_name=None, parentid=1, order=999):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/create'
        param = {'access_token': WeWork.get_contact_token()}
        headers = {'content-type': 'charset=utf-8'}
        if depart_name == None:
            depart_name = "子部门" + str(calendar.timegm(time.gmtime()))
        json = {
            "name": depart_name,
            "parentid": parentid,
            "order": order
        }
        resp = super().request_api('POST', url, params=param, json=json, headers=headers)
        return resp

    def update_department(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/update'
        param = {'access_token': WeWork.get_contact_token()}
        headers = {'content-type': 'charset=utf-8'}
        depart_name = "改个名" + str(calendar.timegm(time.gmtime()))
        json = {
            "id": 5,
            "name": depart_name,
            "parentid": 1,
            "order": 9999
        }
        resp = super().request_api('POST', url, params=param, json=json, headers=headers)
        return resp

    def delete_department(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/delete'
        param = {
            'access_token': WeWork.get_contact_token(),
            "id": 3
        }
        headers = {'content-type': 'charset=utf-8'}
        resp = super().request_api('GET', url, params=param, headers=headers)
        return resp