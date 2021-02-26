"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/2/26 9:02 下午'
"""
from web.podemo.index_page import IndexPage


class TestRegister:
    def setup(self):
        self.index = IndexPage()

    def test_register(self):
        # assert self.index.goto_login().goto_register().register()
        assert self.index.goto_register().register()