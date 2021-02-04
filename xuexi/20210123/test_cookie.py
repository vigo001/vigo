#!/usr/bin/env python
# _*_coding: utf-8 _*_
""""以Google浏览器为例：

首先打开cmd，使用命令启动一个Debug监听端口的浏览器（启动前要先关闭chrome所以窗口）

C:\Program Files (x86)\Google\Chrome\Application>chrome --remote-debugging-port=9222
然后在打开的浏览器打开url地址：

https://testerhome.com/teams"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestTestdemo():
    def setup_method(self, method):

         options = Options()
         options.debugger_address = "127.0.0.1:9222"
         self.driver = webdriver.Chrome(options=options)

    def teardown_method(self, method):
         self.driver.quit()

    def test_testdeom(self):
        self.driver.get("https://www.baidu.com/")
        sleep(3)
