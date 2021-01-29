# -*- coding: utf-8 -*-
# @Author : feier
# @File : test_fixture.py
import pytest

@pytest.fixture()
def login():
    print('登录操作')
    print('获取 token')
    username = "tom"
    password = "123456"
    token = "token173u3hkjm"
    # yield 关键字可以激活 fixture 的 teardown 功能
    # yield 相当于 return，返回数据可以直接跟在 yield 后面
    yield [username, password, token]
    print("注销操作")



# 测试用例1：需要提前登录
# 在测试用例中传入 fixture 方法名
def test_case1(login):
    # 获取fixture 方法的返回值，直接调用fixture方法名
    print(f"用户信息为:{login}")
    print('测试用例1')

def test_case2(connectDB):
    print('测试用例2')

# 测试用例3：需要提前登录
def test_case3():
    print('测试用例3')

# 测试用例4：需要提前登录
@pytest.mark.usefixtures("login")
def test_case4():
    print('测试用例4')