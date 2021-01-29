# -*- coding: utf-8 -*-
# @Author : feier
# @File : test_demo1.py

import pytest

@pytest.fixture()
def connectDB():
    print("test_demo1 中的 connect DB")

def test_a(connectDB):
    print("sub_demo test_a")

class TestA:
    def test_b(self):
        print("sub_demo test_b")