#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from gift import have_gift
import gift


# 发礼物方法
def send():
    print("发礼物啦")
    # have_gift = True
    # print(id(have_gift))
    gift.have_gift = True
    print(id(gift.have_gift))
