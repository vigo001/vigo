#!/usr/bin/env python
# _*_coding: utf-8 _*_

import pytest

@pytest.fixture()
def login():
    print("这是一个登入方法")
    return ('tome', '123')

@pytest.fixture()
def operate():
    print("登入后操作")

def test_case1(login,operate):
    print(login)
    print("test_case1,需要登入")

def test_case2():
    print("test_case2,不需要登入")

def test_case3(login):
    print(login)
    print("test_case3,需要登入")



