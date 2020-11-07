#!/usr/bin/env python
# _*_coding: utf-8 _*_
import shelve
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestTestdemo():
    def setup_method(self):
        options = Options()
        options.debugger_address = '127.0.1:9222'
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        self.driver.quit()

    def test_cookie(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def test_cookie(self):
        # cookies = self.driver.get_cookies()
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688850280623055'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': '9ty12OfXwe-tlvSL6f_xUOYXkNANzElWuSLK7MJprx8exI4lBVrYplNfkW2z67wDB7Nu5RO9udLcgKEiFgJcTxY6IYi1G7mT2hQS_2WN1XTWok9E7pPlWxf-PYgzwxudh72yq5ywlcFfKj1LSKaUDyFyLPYmfyIUUa961E84TXh_Wa8jfwWItwdL9uGnWsyq2BeEkrihrXpdx2LeRwz3fQOfctXytpix3MTQen6UMgIki7R_qB0tCu39S7yNp4610tOrvE6708uB7NDvrmQ8jw'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688850280623055'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325065179391'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a5048037'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'VyAWKCoDKOzjzq95NQ8s2058NCn-sQoAc0fbxrkop64yLKQE8rYj64tltMAqK8H6'},
            {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_info', 'path': '/', 'secure': False,
             'value': 'ssid=s7613154616'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '3469797473431313'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1604778971, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': 'eajrql'},
            {'domain': '.qq.com', 'expiry': 1604845228, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.162069707.1604747436'},
            {'domain': '.qq.com', 'expiry': 1667830828, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.723290983.1604747436'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1636283435, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 1606713036, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/',
             'secure': False, 'value': '1229348283'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '7967958306'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1636283928, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1604747704'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1607350830, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.qq.com', 'expiry': 2147483797, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': 'd764da7fa9650b8f27d8741e2536596aa93c6daf52c1ed63ff5d3af67a9996f9'},
            {'domain': '.qq.com', 'expiry': 2147483737, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'nm4sGbEyal'},
            {'domain': '.qq.com', 'expiry': 1604758888, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '68361216'}]
        # db = shelve.open("cookies")
        # db['cookie'] = cookies
        # db.close()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        for cookie in cookies:
            self.driver.add_cookie(cookie)
            # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            self.driver.refresh()
        time.sleep(4)
