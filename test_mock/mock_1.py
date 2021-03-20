"""Send a reply from the proxy without sending any data to the remote server."""
import json

from mitmproxy import http

from mitmproxy import ctx


class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow: http.HTTPFlow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)
        # 判断是否是想要的请求信息，通过url进行判断

    def response(self, flow):
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" \
                in flow.request.pretty_url:
        # 修改原始数据
        # 获取的text 是str类型，如果要对数据进行操作，需要进行数据转换
            data = json.loads(flow.response.text)
            data["data"]["items"][0]["quote"]["name"] = "hogwarts"
            data["data"]["items"][1]["quote"]["name"] = "hogwarts"
            data["data"]["items"][2]["quote"]["name"] = "hogwarts"
            flow.response.text = json.dumps(data)
        # 赋值给响应信息


addons = [
    Counter()
]