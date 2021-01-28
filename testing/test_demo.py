# -*- coding: utf-8 -*-
# @Author  : feier
# @File    : test_demo.py
import pytest


def test_a():
    print("test_demo.py  test_a")


def test_b():
    print("test_demo.py  test_b")


def test_c():
    assert 1 == 2


@pytest.mark.parametrize('a', [1, 2, 3])
@pytest.mark.parametrize('b', [4, 5, 6])
def test_param(a, b):
    print(f"a = {a}, b = {b}")
