# -*- coding: utf-8 -*-
# @Author : feier
# @File : test_calc_new.py
import allure
import pytest
import yaml

with open("./datas/calc.yaml") as f:
    datas = yaml.safe_load(f)['add']
    add_datas = datas['datas']
    print(add_datas)
    myid = datas['myid']
    print(myid)

@pytest.fixture(params=add_datas, ids=myid)
def get_datas(request):
    print('开始计算')
    data = request.param
    print(f"测试数据为：{data}")
    yield data
    print("结束计算")

# 文件名以test_开头， 类名以Test开头， 方法名以test_开头
# 注意：测试类里一定不要加__init__()方法
@allure.feature("测试计算器")
class TestCalc:
    '''
    优化点：
    1. 把 setup 和teardown 换成了 fixture 方法 get_calc
    2. 把 get_calc 方法放到 conftest 中
    3. 把参数化换为了 fixture 参数化方式
    4. 测试用例中的数据需要通过 get_datas 获取
    get_datas 返回了一个列表[0.1,0.2,0.3]，分别代表了a,b,expect
    '''

    @allure.story("测试加法")
    @pytest.mark.add
    def test_add(self, get_calc, get_datas):
        # 调用相加方法
        with allure.step("计算两个数的相加和"):
            result = get_calc.add(get_datas[0], get_datas[1])
        if isinstance(result, float):
            result = round(result, 2)
        # 得到相加结果之后写断言
        assert result == get_datas[2]