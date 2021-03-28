import json

import requests

from test_requests_lagou.wework.base import Base


class Address(Base):
    def get_member_information(self, user_id):
        get_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        params = {
            "userid": user_id
        }
        r = self.send("GET", get_member_url, params=params)
        return r.json()

    def update_member(self, user_id, name, mobile):
        update_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        data = {
            "userid": user_id,
            "name": name,
            "mobile": mobile,
        }
        r = self.send("POST",url=update_member_url, json=data)
        return r.json()

    def create_member(self, user_id, name, mobile, department):
        create_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        data = {
            "userid": user_id,
            "name": name,
            "mobile": mobile,
            'department': department
        }
        r = self.send("POST", url=create_member_url, json=data)
        return r.json()

    def delete_member(self, userid):
        delete_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        params = {"userid": userid}
        r = self.send("GET", delete_url, params=params)
        return r.json()

def test_data():
    data = {'a': 20}
    r = requests.post("https://httpbin.org/post",data=data)
    print(r.json())