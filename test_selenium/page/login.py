#!/usr/bin/env python
# _*_coding: utf-8 _*_

from selenium.webdriver.common.by import By
from test_selenium.page.base_page import BasePage
from test_selenium.page.register import Register

class Login(BasePage):
    def scan_qrcode(self):
        pass

    def goto_register(self):
        self._driver.find_element(By.LINK_TEXT, "企业注册").click()
        return Register