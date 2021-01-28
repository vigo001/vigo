#!/usr/bin/env python
# _*_coding: utf-8 _*_

def add(x, y):
    return x + y


def test_add():
    assert add(1, 10) == 11
    assert add(1, 1) == 2
    assert add(1, 99) == 100


class TestClass:

    def test_one(self):
        x == "this"
        assert "h" in x

    def test_one(self):
        x = "hello"
        assert hasattr(x, "check")
