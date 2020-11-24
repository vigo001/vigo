#!/usr/bin/env python
# _*_coding: utf-8 _*_
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from web.podemo.register_page import RegisterPage

class LoginPge:
    def __int__(self, driver: WebDriver):
        self.driver = driver

    # 扫码
    def scan(self):
        pass

    # 进入注册页
    def goto_register(self):
        self.driver.find_element(By.CSS_SELECTOR, ".login_registerBar_link").click()
        return RegisterPage(self.driver)




