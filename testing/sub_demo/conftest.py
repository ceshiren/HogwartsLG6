# -*- coding: utf-8 -*-
# @Author : feier
# @File : conftest.py
import pytest

@pytest.fixture()
def connectDB():
    print("sub_demo 下面的 connect DB")