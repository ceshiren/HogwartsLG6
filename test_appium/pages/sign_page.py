from appium.webdriver.common.mobileby import MobileBy

from test_appium.pages.basepage import BasePage


class SignPage(BasePage):

    def sign(self):
        # self.find_click("//*[@text='外出打卡']")
        # self.find_click("//*[contains(@text,'次外出')]")
        #
        # # 获取元素的text属性
        # self.find("//*[@text='外出打卡成功']")
        self.parse_action("../pages/sign_page.yaml", "sign")

    def first_sign(self):
        # self.find_click("//*[@text='上下班打卡']")
        self.parse_action("../pages/sign_page.yaml", "first_sign")
