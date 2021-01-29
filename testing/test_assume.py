# -*- coding: utf-8 -*-
# @Author : feier
# @File : test_assume.py
import pytest


def test_a():
    # assert 1 == 2
    # assert False  == True
    # assert 100 == 200
    pytest.assume(1 == 1)
    pytest.assume(False == True)
    pytest.assume(100 == 200)
    pytest.assume(3 == 1)