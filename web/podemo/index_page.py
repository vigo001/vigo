#!/usr/bin/env python
# _*_coding: utf-8 _*_
from selenium import webdriver
from selenium.webdriver.common.by import By
from web.podemo.loginpage import LoginPge
from web.podemo.register_page import RegisterPage


class Indexpage:
    def __int__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")

    def goto_login(self):
        # click login
        self.driver.find_element(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        # return login
        return LoginPage(self.driver)

    def goto_register(self):
        # click singup
        self.driver.find_element(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return RegisterPage(self.driver)
        pass
