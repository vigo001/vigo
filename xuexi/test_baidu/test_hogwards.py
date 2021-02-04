#!/usr/bin/env python
# _*_coding: utf-8 _*_

from selenium import webdriver
import time


class TestHogwards():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_hogwards(self):
        self.driver.get("https://ceshiren.com/")
        time.sleep(2)
        self.driver.find_element_by_class_name("//*[@id='navigation-bar']//li[4]").click()
