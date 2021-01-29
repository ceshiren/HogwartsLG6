# -*- coding: utf-8 -*-
# @Author : feier
# @File : test_ordering.py
from time import sleep

import pytest

@pytest.mark.run(order=10)
def test_1():
    sleep(1)
    assert True

#@pytest.mark.third
def test_2():
    sleep(1)
    assert True

@pytest.mark.run(order=9)
def test_3():
    sleep(1)
    assert True