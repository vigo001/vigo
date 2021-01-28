#!/usr/bin/env python
# _*_coding: utf-8 _*_
import pytest


@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [8, 10, 11])
def test_foo(x, y):
    print(f"测试数据组合x:{x},y:{y}")
