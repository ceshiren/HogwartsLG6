from test_appium.pages.basepage import BasePage
from test_appium.pages.work_page import WorkPage


class InformationPage(BasePage):
    def goto_work_page(self):
        # self.find_click("//*[@text='工作台']")
        self.parse_action("../pages/information_page.yaml", "goto_work_page")
        return WorkPage(self.driver)
