"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/12 8:20 下午'
"""
from test_appium.pages.basepage import BasePage
from test_appium.pages.editcontact_page import EditContactPage


class AddContactPage(BasePage):
    def addcontact_menual(self):
        # 点击手动输入添加
        self.parse_action("../pages/addcontact_page.yaml", "addcontact_menual")
        return EditContactPage(self.driver)
