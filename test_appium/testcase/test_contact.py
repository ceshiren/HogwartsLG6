"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/12 8:38 下午'
"""
import yaml

from test_appium.pages.app import App


class TestContact:
    def setup(self):
        self.app = App()

    def test_addcontact(self):
        name = "hogwarts_104"
        phonenum = "13211111112"
        editpage = self.app.goto_main().goto_addresslist().click_addcontact().addcontact_menual()
        editpage.edit_contact(name,phonenum)
        editpage.verify_ok()

