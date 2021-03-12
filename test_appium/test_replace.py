"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/12 8:57 下午'
"""
import logging


def test_replace():
    a = {'name': "哈利波特", 'phonenum':'13911111111'}
    b = "hogwarts hogwarts ${name}  hogwarts hogwarts  ${phonenum}"

    for key,value in a.items():
        x = "${"+key+"}"
        print(x)
        b = b.replace(x, value)

    print(b)

def test_log():
    root_log = logging.getLogger(__name__)
    print(root_log.handlers)
    for h in root_log.handlers[:]:
        root_log.removeHandler(h)
        h.close()
    logging.basicConfig(level=logging.INFO)

    logging.info("aaa")