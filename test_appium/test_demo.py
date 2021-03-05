# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "wework"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        # 不清空缓存启动app
        caps["noReset"] = "true"
        # 设置等待页面空闲状态的时间为0s
        caps['settings[waitForIdleTimeout]'] = 0
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 显式等待10s
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_demo(self):
        el1 = self.driver.find_element_by_id("com.tencent.wework:id/guu")
        el1.click()
        el2 = self.driver.find_element_by_id("com.tencent.wework:id/fk1")
        el2.send_keys("张一")
        el3 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]")
        el3.click()
        el4 = self.driver.find_element_by_id("com.tencent.wework:id/dx1")
        el4.send_keys("测试")
        el5 = self.driver.find_element_by_id("com.tencent.wework:id/dwx")
        el5.click()

    def test_daka(self):
        self.driver.find_element_by_xpath("//*[@text='工作台']").click()
        # 滚动查找元素
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("打卡").instance(0));').click()
        self.driver.find_element_by_xpath("//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'次外出')]").click()
        # 获取元素的text属性

        # r = self.driver.find_element_by_id("com.tencent.wework:id/mn").text
        self.driver.find_element_by_xpath("//*[@text='外出打卡成功']")
