"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/2/26 8:32 下午'
"""
from selenium.webdriver.common.by import By

# 登录页面的PO
from selenium.webdriver.remote.webdriver import WebDriver

from web.podemo.register_page import RegisterPage


class LoginPage:
    def __init__(self,driver:WebDriver):
        self.driver = driver

    def scan(self):
        '''
        扫码
        :return:
        '''
        pass

    def goto_register(self):
        # click register link
        self.driver.find_element(By.CSS_SELECTOR, ".login_registerBar_link").click()
        # return RegisterPage()
        return RegisterPage(self.driver)

