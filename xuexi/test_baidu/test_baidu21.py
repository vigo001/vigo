#!/usr/bin/env python
# _*_coding: utf-8 _*_
from selenium import webdriver


def test_search():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    search = driver.find_element_by_id("su").get_attribute('vaule')
    assert search == "百度"
