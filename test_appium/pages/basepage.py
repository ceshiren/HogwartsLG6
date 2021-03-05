from typing import List, Dict

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_click(self, locator):
        self.find(locator).click()

    def find(self, locator):
        return self.driver.find_element_by_xpath(locator)

    def swip_click(self, text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));').click()

    def parse_action(self, path, fun_name):
        with open(path, "r", encoding="utf-8") as f:
            funciton = yaml.safe_load(f)
            steps: List[Dict] = funciton[fun_name]
        for step in steps:
            if step["action"] == "find_click":
                self.find_click(step["locator"])
            elif step["action"] == "find":
                self.find(step["locator"])
