#!/usr/bin/env python
# _*_coding: utf-8 _*_
import pytest
import yaml


@pytest.mark.parametrize("a, b", yaml.safe_load(open("data.yml", encoding='utf-8')))
def test_foo(a, b):
    print(f"a + b = {a + b}")
