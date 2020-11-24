#!/usr/bin/env python
# _*_coding: utf-8 _*_
from web.podemo.index_page import Indexpage


class TestWeiXin:

    def setup(self):
        self.index = Indexpage()

    def test_register(self):
        assert self.index.goto_register().register()
