#!/usr/bin/env python3
#-*- coding: utf-8 -*-
"""
@Project : WeworkApiTest
@File    : test_department.py
@Time    : 2019-11-06  08:22:00
@Author  : indeyo_lin
@Version : 
@Remark  :
"""
import time
import calendar

from jsonpath import jsonpath

from api.department import Department

class TestDepartment:

    # def setup(self):
    #     self.department = Department()
    #     self.list = self.department.get_department_list()

    department = Department()

    def test_get_department_list(self):
        list = self.department.get_department_list()
        assert list['errcode'] == 0

    def test_create_department(self):
        depart_name = "子部门" + str(calendar.timegm(time.gmtime()))
        repr = self.department.create_department(depart_name, 1, 999)
        list = self.department.get_department_list()
        # print(jsonpath(list, "$..department[?(@.id==%s)]" % repr['id'])[0]['name'])
        # print(jsonpath(list, "$..department[?(@.id==%s)]" % repr['id']))
        assert repr['errcode'] == 0
        assert jsonpath(list, "$..department[?(@.id==%s)]" % repr['id'])[0]['name'] == depart_name

    def test_update_department(self):
        repr = self.department.update_department(5)
        assert repr['errcode'] == 0

    def test_delete_department(self):
        """TODO:有前置条件，每次执行前需要有存在的部门id"""
        repr = self.department.delete_department(4)
        assert repr['errcode'] == 0


