"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/3/12 9:56 下午'
"""
import logging

root_log = logging.getLogger(__name__)
# for h in root_log.handlers[:]:
#     root_log.removeHandler(h)
#     h.close()

logging.basicConfig(level=logging.INFO,
                    # 日志格式
                    # 时间、代码所在文件名、代码行号、日志级别名字、日志信息
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    # 打印日志的时间
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    # 日志文件存放的目录（目录必须存在）及日志文件名
                    filename='report.log',
                    # 打开日志文件的方式
                    filemode='a'
                    )