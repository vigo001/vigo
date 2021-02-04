#!/usr/bin/env python
# _*_coding: utf-8 _*_
from selenium import webdriver
from time import sleep
from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    def __init__(self, driver: WebDriver = None):
        #此处对driver进行复用，如果不存driver就构造一个新的
        if driver is None:
            # index页面需要用，首次使用时构造新driver
            self._driver = webdriver.Chrome()
            # 设置隐式等待时间
            self._driver.maximize_window()
            self._driver.implicitly_wait(5)
            # 访问网页
            self._driver.get(self._base_url)
        else:
            self._driver = driver
    def close(self):
        sleep(20)
        self._driver.quit()

