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

from api.department import Department

class TestDepartment:

    department = Department()

    def test_get_department_list(self):
        list = self.department.get_department_list()
        assert list['errcode'] == 0

    def test_create_department(self):
        repr = self.department.create_department()
        assert repr['errcode'] == 0
        assert repr['id'] != ""

    def test_update_department(self):
        repr = self.department.update_department()
        assert repr['errcode'] == 0

    def test_delete_department(self):
        """TODO:有前置条件，每次执行前需要有存在的部门id"""
        repr = self.department.delete_department()
        assert repr['errcode'] == 0


