#!/usr/bin/env python
# _*_coding: utf-8 _*_

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    base_url = ""

    def __int__(self, driver: WebDriver = None):
        if driver == None:
            options = Options()
            options.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=options)
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver
        if self.base_url != "":
            self.driver.get(self.base_url)

    def find(self, by, locator):
        return  self.driver.find_element(by,locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)
    def wait_for_click(self, locator, timeout=10):
        element:WebElement = WebDriverWait(self.driver,timeout).until(
            expected_conditions.element_to_be_clickable(locator))
        return element