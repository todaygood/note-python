# session_demo.py

from flask import Flask, session
import os
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)


# 添加数据到session中
# 操作session的时候，跟操作字典是一样的
# SECRET_KEY

@app.route('/')
def hello_world():
    session['username'] = 'zhiliao'
    # 如果没有指定session的过期时间，那么默认是浏览器关闭后就自动结束
    # 如果设置了session的permanent属性为True，那么过期时间是31天。
    session.permanent = True
    return "in / &session={} username={}".format(hex(id(session)), session.get('username'))


@app.route('/get/')
def get():
    return "in /get/ &session={} username={}".format(hex(id(session)), session.get('username'))


@app.route('/delete/')
def delete():
    print(session.get('username'))
    session.pop('username')
    print(session.get('username'))
    return 'success'


@app.route('/clear/')
def clear():
    print(session.get('username'))
    # 删除session中的所有数据
    session.clear()
    print(session.get('username'))
    return 'success'


if __name__ == '__main__':
    app.run(debug=True)
