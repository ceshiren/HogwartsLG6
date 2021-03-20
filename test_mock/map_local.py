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
        # 打开文件，读取文件数据，作为响应，给返回
            with open("tmp2.json", encoding="utf-8") as f:
                data = json.load(f)
            flow.response.text = json.dumps(data)


addons = [
    Counter()
]