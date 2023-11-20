
## 测试 Flask 应用

http://docs.jinkan.org/docs/flask/testing.html


[flask单元测试](https://juejin.cn/post/6844904053260959757),(https://flask.palletsprojects.com/en/2.2.x/testing/)

常用的断言方法：
assertEqual     如果两个值相等，则pass
assertNotEqual  如果两个值不相等，则pass
assertTrue      判断bool值为True，则pass
assertFalse     判断bool值为False，则pass
assertIsNone    不存在，则pass
assertIsNotNone 存在，则pass

作者：DevOps海洋的渔夫
链接：https://juejin.cn/post/6844904053260959757
来源：稀土掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


flask框架的核心对象有:
Flask,AppContext,Map, RequestContext,Request,Response,Rule,Blueprint,session,_AppCtxGlobals;

Flask主要管理着AppContext，RequestContext，以及所有的请求的处理步骤；

AppContext为应用上下文对象，主要管理app对象的获取和请求的临时状态存储变量g；

RequestContext为请求上下文，主要管理Request对象和保存会话的session对象；

Request为请求对象，在发生请求是随着RequestContext被创建而创建，管理着请求数据和Rule对象；

Response为响应对象，在应用逻辑处理完毕后创建，管理着响应数据和响应方法；

Rule路由对象，管理着路由和视图处理函数的标识符的对应关系；

Map对象管理着所有的标识符和其视图函数对象的一一对应关系；

Blueprint对象，Flask对象的缩小版，主要是为了对大量的视图函数做分类管理；

session为保存会话信息的容器，可以看做一个字典；

_AppCtxGlobals即g变量，用来在每次请求中临时存储资源，它属于应用上下文的一个属性。


flask unittest时 app何时run的？

https://blog.csdn.net/luanpeng825485697/article/details/102667745


运行:

 pytest -q test_params.py

执行测试时需要下面几步：

从命令行进入测试文件所在目录，pytest会在该目录中寻找以test开头的文件
测试类以Test开头，并且不能带有__init__方法
找到测试文件，进入测试文件中寻找以test_开头的函数并执行
测试函数以断言assert结尾
————————————————
版权声明：本文为CSDN博主「腾讯数据架构师」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/luanpeng825485697/article/details/102667745


TestCase：一个testcase就是一条测试用例。
setUp：测试环境的准备
tearDown：测试环境的还原
run：测试执行
TestSuite：测试套件或集合，多个测试用例的集合就是1个suite，一个suite可以包含多条测试用例，测试套件suite里面也可以嵌套测试套件suite
TestLoader：用来加载testcase与testsuite
Testrunner：用来执行测试用例，将测试结果保存在texttestresult中
2、注意：

class继承unittest.TestCase，继承后就形成了一条测试用例。如果在class中有多个test开头的 方法，那么每个test开头的方法，在load的时候，便会生成一条testcase。
模块名以test开头
类以Test开头
方法以test开头
运行时，右击出现unittest。如果没有出现，那么需要配置
或者使用python运行，添加： if __name__ == ‘__main__’: unittest.main()
3、断言结果：

. 表示通过 或者 pass
F False, 表示断言没有通过
E Error, 表示程序内部发生了错误。
4、执行顺序：

根据 ascii 编码排序
如果我们想手工调整测试用例的执行顺序，不同的字母前面加 数字。
5、pycharm 运行时注意事项：

在空行处右击，执行整个模块
在类名上， 执行单个测试类
在方法名上， 执行单个测试用例
注意在指定的位置运行，空行的地方去运行。
以上就是本文的全部内容，希望对大家的学习有所





## flask template 


https://blog.csdn.net/shangxiaqiusuo1/article/details/103684463

datetime.timedelta  


## 前后端 http数据传输

json/form

https://blog.csdn.net/weixin_43262264/article/details/116268715


## flask 操作数据库

https://github.com/gnu4cn/flaskLearnings/blob/master/10_flask-SQLAlchemy.md


## flask session 

[flask session](https://blog.csdn.net/phoenix339/article/details/96427336),https://blog.csdn.net/qq_25672165/article/details/114581467

https://blog.csdn.net/legend818/article/details/117367760

from datetime import timedelta
 
session.permanent = True
app.permanent_session_lifetime = timedelta(minutes=5)
session['key'] = value




## 发送http请求哪个库适合我？

https://blog.csdn.net/joye123/article/details/93983121

https://blog.csdn.net/csdnzzu/article/details/80649015

[http response](https://www.cnblogs.com/zhuchunyu/p/10466509.html)

## 线程池

https://www.cnblogs.com/xiaozi/p/6182990.html



## issue ： flask程序测试搞不定

FAILED (errors=1)

Error
Traceback (most recent call last):
  File "D:\PycharmProjects\eagleeye\server\test_server_api.py", line 27, in test_login
    response = self.client.post('/login', data=json.dumps(user_info_dict), content_type='application/json')
  File "D:\PycharmProjects\eagleeye\venv\lib\site-packages\werkzeug\test.py", line 1145, in post
    return self.open(*args, **kw)
  File "D:\PycharmProjects\eagleeye\venv\lib\site-packages\flask\testing.py", line 223, in open
    response = super().open(
  File "D:\PycharmProjects\eagleeye\venv\lib\site-packages\werkzeug\test.py", line 1094, in open
    response = self.run_wsgi_app(request.environ, buffered=buffered)
  File "D:\PycharmProjects\eagleeye\venv\lib\site-packages\werkzeug\test.py", line 961, in run_wsgi_app
    rv = run_wsgi_app(self.application, environ, buffered=buffered)
  File "D:\PycharmProjects\eagleeye\venv\lib\site-packages\werkzeug\test.py", line 1242, in run_wsgi_app
    app_rv = app(environ, start_response)
  File "D:\PycharmProjects\eagleeye\venv\lib\site-packages\flask\app.py", line 2548, in __call__
    return self.wsgi_app(environ, start_response)
  File "D:\PycharmProjects\eagleeye\venv\lib\site-packages\flask\app.py", line 2528, in wsgi_app
    response = self.handle_exception(e)
  File "D:\PycharmProjects\eagleeye\venv\lib\site-packages\flask\app.py", line 2525, in wsgi_app
    response = self.full_dispatch_request()
  File "D:\PycharmProjects\eagleeye\venv\lib\site-packages\flask\app.py", line 1822, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "D:\PycharmProjects\eagleeye\venv\lib\site-packages\flask\app.py", line 1820, in full_dispatch_request
    rv = self.dispatch_request()
  File "D:\PycharmProjects\eagleeye\venv\lib\site-packages\flask\app.py", line 1796, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)
  File "D:\PycharmProjects\eagleeye\server\server_api.py", line 177, in login
    user_info_dict = my_db.query_user_info(username)
NameError: name 'my_db' is not defined


## json 加注释

https://blog.csdn.net/Dream_fengyuefei/article/details/92626804



    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ...',
        'cookie': '_fbp=fb.1.1654447470850.2143140577; _ga=GA1.2.1...'
    }
    response = requests.get(url, headers=headers)

## 学习http协议的好网站httpbin.org

httpbin.org
 0.9.2 
[ Base URL: httpbin.org/ ]
A simple HTTP Request & Response Service.

Run locally: $ docker run -p 80:80 kennethreitz/httpbin

the developer - Website

## httpie ,httpstatus 


## python Requests

利用 Session 我们可以做到模拟同一个会话，而且不用担心 Cookies 的问题，通常用于模拟登录成功之后再进行下一步的操作。


import requests
response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))
print(response.status_code)

若代理需要使用 HTTP Basic Auth，可以使用类似 http://user :password@host:port 这样的语法来设置代理。