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

from api.base_api import BaseApi
from api.wework import WeWork

logging.basicConfig(level=logging.INFO)

class Department(BaseApi):

    list_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list'
    create_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/create'
    update_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/update'
    delete_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/delete'
    param = {'access_token': WeWork.get_contact_token()}
    headers = {'content-type': 'charset=utf-8'}

    def get_department_list(self):
        resp = super().request_api('GET', self.list_url, params=self.param).json()
        super().json_format(resp)
        return resp

    def create_department(self, depart_name=None, parentid=1, order=999):
        if depart_name == None:
            depart_name = "子部门" + str(calendar.timegm(time.gmtime()))
        json = {
            "name": depart_name,
            "parentid": parentid,
            "order": order
        }
        resp = super().request_api('POST', self.create_url, params=self.param, json=json, headers=self.headers).json()
        super().json_format(resp)
        return resp

    def update_department(self):
        depart_name = "改个名" + str(calendar.timegm(time.gmtime()))
        json = {
            "id": 5,
            "name": depart_name,
            "parentid": 1,
            "order": 9999
        }
        resp = super().request_api('POST', self.update_url, params=self.param, json=json, headers=self.headers).json()
        super().json_format(resp)
        return resp

    def delete_department(self):
        param = {
            'access_token': WeWork.get_contact_token(),
            "id": 3
        }
        resp = super().request_api('GET', self.delete_url, params=param, headers=self.headers).json()
        super().json_format(resp)
        return resp