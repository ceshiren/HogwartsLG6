from appium.webdriver.common.mobileby import MobileBy

from test_appium.pages.basepage import BasePage
from test_appium.pages.sign_page import SignPage


class WorkPage(BasePage):

    def goto_sign_page(self):
        # 滚动查找元素
        self.swip_click("打卡")
        return SignPage(self.driver)
