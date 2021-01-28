# -*- coding: utf-8 -*-
# @Author  : feier
# @File    : test_calc.py
import pytest

from python_code.calc import Calculator

def test_a():
    print("测试用例a")

def func():
    print("普通函数")

with open("./datas/calc.yaml") as f:
    datas = yaml.safe_load(f)['add']
    add_datas = datas['datas']
    print(add_datas)
    myid = datas['myid']
    print(myid)

# 文件名以test_开头， 类名以Test开头， 方法名以test_开头
# 注意：测试类里一定不要加__init__()方法    
class TestCalc:
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()
    
    def teardown_class(self):
        print("计算结束")
    
    @pytest.mark.parametrize(
        "a, b, expect",
        add_datas, ids=myid
    )
    def test_add(self, a, b, expect):
        # 实例化计算器类
        # calc = Calculator()
        # 定义一个变量接收add方法的返回值
        # 调用相加方法
        result = self.calc.add(a, b)
        if isinstance(result, float):
            result = round(result,2)
        # 得到相加结果之后写断言
        assert result == expect

    def test_add1(self):
        # calc = Calculator()
        result = self.calc.add(0.1,0.1)
        assert result == 0.2
    
    def test_add2(self):
        # calc = Calculator()
        result = self.calc.add(-1,-1)
        assert result == -2

    def test_add3(self):
        result = self.add(0.1, 0.2)
        assert round(result,2) == 0.3


