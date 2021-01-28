#!/usr/bin/env python
# _*_coding: utf-8 _*_
import pytest

test_user_data = ['Tome', 'Jerry']


@pytest.fixture(scope="module")
def login_r(request):
    user = request.param
    print(f"\n 登入用户：{user}")
    return user


@pytest.mark.parametrize("login_r", test_user_data, indirect=True)
def test_login(login_r):
    a = login_r
    print(f"测试用例中login的返回值：{a}")
    assert a != ""
