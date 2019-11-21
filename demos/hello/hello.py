import click
from flask import Flask

#创建Flask类实例
app = Flask(__name__)

#注册路由（将访问地址与函数名称绑定）
@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'