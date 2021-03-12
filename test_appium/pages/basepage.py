import json
from typing import List, Dict

import allure
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from test_appium.conftest import root_log


class BasePage:
    # 定义一个字典，要替换的内容放在一个字典里
    _params = {}
    _blacklist = [(MobileBy.ID, 'com.tencent.wework:id/ig0'),
                  (MobileBy.XPATH, '//*[@text="关闭"]')
                  ]
    _max_num = 3
    _error_num = 0


    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_click(self, by, locator):
        self.find(by, locator).click()

    def setup_implicitly_wait(self, timeout):
        self.driver.implicitly_wait(timeout)

    def find(self, by, locator):
        # root_log.info("find")
        # root_log.info(by)
        root_log.info(f"find: by={by} , locator = {locator}")
        try:
            element = self.driver.find_element(by, locator)
            self._error_num = 0
            self.setup_implicitly_wait(10)
            return element
        except Exception as e:
            root_log.error("未找到元素")
            # 处理黑名单逻辑
            self.setup_implicitly_wait(2)

            self.driver.get_screenshot_as_file("tmp.png")
            allure.attach.file("tmp.png",attachment_type=allure.attachment_type.PNG)
            # 设置最大查找次数
            if self._error_num > self._max_num:
                self._error_num = 0
                self.setup_implicitly_wait(10)
                raise e
            # 每次进except 一次都执行+1操作
            self._error_num += 1
            # 处理黑名单
            for ele in self._blacklist:
                # find_elements 会返回元素的列表[ele1,ele2.....]，如果没有元素会返回一个空列表
                eles = self.driver.find_elements(*ele)
                if len(eles) > 0:
                    eles[0].click()
                    return self.find(by, locator)
            # 如果黑名单都处理完，仍然没有找到想要的元素，则抛出异常
            raise e

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

        # json 序列化与反序列化
        # json.dumps() 序列化  python 对象转化成字符串
        # json.loads() 反序列化  python 字符串转化为python对象
        raw = json.dumps(steps)
        for key, value in self._params.items():
            raw = raw.replace("${" + key + "}", value)
        steps = json.loads(raw)
        for step in steps:
            if step["action"] == "find_click":
                self.find_click(step["by"], step["locator"])
            elif step["action"] == "find":
                self.find(step["by"], step["locator"])
            elif step["action"] == "swip_click":
                self.swip_click(step["text"])
            elif step["action"] == "find_sendkeys":
                self.find(step["by"], step["locator"]).send_keys(step["text"])
