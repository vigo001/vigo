#!/usr/bin/env python
# _*_coding: utf-8 _*_
import pytest


@pytest.fixture()
def login():
    print("这时一个登入的方法")
    return ('tome', '123')


@pytest.fixture()
def operate():
    print("这是登入后的操作")


def test_case1(login, operate):
    print(login)
    print("test_case1,需要登入")


def test_case2():
    print("test_case2,不需要登入")


def test_case3(login):
    print(login)
    print("test_case3,需要登入")
