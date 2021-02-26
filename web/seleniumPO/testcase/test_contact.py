"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/2/26 9:37 下午'
"""
from web.seleniumPO.page.main_page import MainPage


class TestContact:
    def setup(self):
        self.mainpage = MainPage()

    def test_addmember(self):
        username = "aaaa_0005"
        account = "aaaa_0005"
        phonenum = "13012345605"
        page = self.mainpage.goto_add_member()
        page.add_member(username, account, phonenum)
        names = page.get_member()
        print(names)
        assert username in names

    def teardown(self):
        self.mainpage.quit_driver()
