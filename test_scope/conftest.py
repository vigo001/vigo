#!/usr/bin/env python
# _*_coding: utf-8 _*_

port pytest

def open():
    print("打开浏览器")
    yield
    print("执行teardown !")

