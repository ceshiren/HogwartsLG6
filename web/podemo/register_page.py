"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/2/26 8:32 下午'
"""

# 注册页PO
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RegisterPage():
    # 类型提示
    def __init__(self,driver:WebDriver):
        self.driver = driver

    def register_OK(self):
        '''
        注册
        :return:
        '''

        # 输入[公司名]
        self.driver.find_element(By.ID, "corp_name").send_keys("测吧公司")
        # 输入[管理者姓名]
        self.driver.find_element(By.ID, "manager_name").send_keys("思寒")

        # 输入[电话号码]
        self.driver.find_element(By.ID, "register_tel").send_keys("13012345678")

        # 点击 [注册 ]
        self.driver.find_element(By.ID, "submit_btn").click()

        return True


