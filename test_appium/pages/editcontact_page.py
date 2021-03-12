"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/12 8:22 下午'
"""
from test_appium.pages.basepage import BasePage


class EditContactPage(BasePage):
    def edit_contact(self,name,phonenum):
        '''
        编辑成员
        :return:
        '''
        self._params['name'] = name
        self._params['phonenum'] = phonenum

        self.parse_action("../pages/editcontact_page.yaml", "edit_contact")

    def verify_ok(self):
        self.parse_action("../pages/editcontact_page.yaml", "verify_ok")
