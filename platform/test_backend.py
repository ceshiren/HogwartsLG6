import json

import requests
from flask import jsonify

from backend import TestCase, db


def test_server():
    r = requests.get('http://127.0.0.1:5000')
    print(r.text)
    assert 'ceshiren.com' in r.text


def test_testcase():
    r = requests.get('http://127.0.0.1:5000/testcase')
    size_origin = len(r.json())
    r = requests.post(
        'http://127.0.0.1:5000/testcase',
        json={
            'name': 'demo1',
            'description': 'des1',
            'steps': ['a', 'b', 'c']
        }
    )
    assert r.status_code == 200

    r = requests.get('http://127.0.0.1:5000/testcase')
    size_new = len(r.json())

    assert size_new == size_origin + 1

    r = requests.delete('http://127.0.0.1:5000/testcase', params={'name': "demo1"})
    r = requests.get('http://127.0.0.1:5000/testcase')
    size_new = len(r.json())
    assert size_new == size_origin


def test_testcase_update():
    r = requests.get('http://127.0.0.1:5000/testcase')
    size = len(r.json())
    r = requests.post(
        'http://127.0.0.1:5000/testcase',
        params={"name": 'demo1'},
        json={
            'name': 'demo1',
            'description': 'des2',
            'steps': ['a1', 'b1', 'c1']
        }
    )
    assert r.status_code == 200

    r = requests.get('http://127.0.0.1:5000/testcase')
    size_new = len(r.json())

    assert size_new == size


def test_json():
    # todo: 普通类与json的序列化，找到一个更简单的方式
    testcase = TestCase(name="1", description="1", steps=['a', 'b'])
    # print(json.dumps(testcase.__dict__))
    # print(json.dumps(
    #     testcase,
    #     default=lambda o: o.__dict__ if hasattr(o, '__dict__') else None,
    #     check_circular=False
    # )
    # )

    print(testcase.as_dict())
    print(repr(testcase))

    # print(json.dumps(testcase, default=lambda o: o.__dict__,
    #                  sort_keys=True, indent=4))

    class A:
        def __init__(self, name):
            self.name = name

    a = A(name="aa")
    print(json.dumps(a.__dict__))
    print(json.dumps(a, default=lambda o: o.__dict__))


def test_db_init():
    db.create_all()
    testcase = TestCase.query.first()
    print(testcase)

    # testcase_new = TestCase()
    # testcase_new.name = "testcase demo 1"
    # testcase_new.description = "demo description"
    # db.session.add(testcase_new)
    # db.session.commit()

    testcase_new = TestCase()
    testcase_new.name = "testcase demo 2"
    testcase_new.description = "demo 2 description"
    db.session.add(testcase_new)
    db.session.commit()
