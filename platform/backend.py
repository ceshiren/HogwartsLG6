import json
from typing import List

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lagou6:ceshiren.com@stuq.ceshiren.com:23306/lagou6?charset=utf8mb4'
db = SQLAlchemy(app)
# 开启不同源访问
CORS(app)
testcases = []


@app.route('/')
def hello_world():
    return 'Hello ceshiren.com, World!'


class Main(Resource):
    def get(self):
        return {"body": "ceshiren.com"}

    def post(self):
        pass


# class TestCase(dict):
#     def __init__(self, name: str, description: str, steps: List[str]):
#         self['name'] = name
#         self['description'] = description
#         self['steps'] = steps

class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=True)
    steps = db.Column(db.String(1024), unique=False, nullable=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return json.dumps({
            "id": self.id,
            "name": self.name,
            'steps': self.steps
        })


class TestCaseService(Resource):
    def get(self):
        """
        获取所有的接口测试用例或者单个的测试用例，返回json结构体
        :return:
        """
        # 把返回的数据改成了 json 结构
        # 前端，可以方便的解析 json 结构，方便前端进行展示
        # 前端  -get：获取用例-> 后端
        testcases = [item.as_dict() for item in TestCase.query.all()]
        return testcases

    def post(self):
        """
        新增测试用例，或者修改测试用例，使用post代替put和delete也是很多公司常用做法
        :return:
        """
        app.logger.info(request.args)
        if 'name' in request.args:
            for i in range(len(testcases)):
                if testcases[i]['name'] == request.args['name']:
                    testcases[i] = request.json
        else:
            app.logger.info(request.json)
            testcase = TestCase(**request.json)
            testcase.steps = json.dumps(request.json.get('steps'))
            app.logger.info(testcase)
            # testcases.append(testcase)
            db.session.add(testcase)
            db.session.commit()

            return {
                'size': len(testcases),
                'msg': 'ok',
                'errcode': 0
            }

    def delete(self):
        """
        删除特定用例
        :return:
        """
        # if 'name' in request.args:
        #     for item in testcases:
        #         if item['name'] == request.args['name']:
        #             testcases.remove(item)

        testcase = TestCase.query.filter_by(name=request.args.get('name')).first()
        app.logger.info(testcase)
        db.session.delete(testcase)
        db.session.commit()

        return {
            'errcode': 0
        }

    def put(self):
        """
        新增测试用例，或者修改测试用例，有的时候会通过post来代替put
        :return:
        """

# 指定 url 的作用范围
api.add_resource(Main, '/main')
api.add_resource(TestCaseService, '/testcase')

if __name__ == '__main__':
    app.run(debug=True)
