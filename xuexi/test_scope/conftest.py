#!/usr/bin/env python
# _*_coding: utf-8 _*_

import pytest

@pytest.fixture(scope="session")
def open():
    print("打开浏览器")
    yield

    print("执行teardown ！")
    print("关闭浏览器")
