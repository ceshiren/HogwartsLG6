# -*- coding: utf-8 -*-
# @Author : feier
# @File : conftest.py
import pytest
from python_code.calc import Calculator


@pytest.fixture(scope="session")
def connectDB():
    print("连接数据库操作")
    yield
    print("断开数据库连接")


@pytest.fixture(scope='class')
def get_calc():
    print('获取计算器实例')
    calc = Calculator()
    return calc