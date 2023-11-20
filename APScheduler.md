


APScheduler

[Python 定时任务框架 APScheduler 详解](https://www.cnblogs.com/leffss/p/11912364.html)


session=eyJfcGVybWFuZW50Ijp0cnVlLCJ1aWQiOjMsInVzZXJuYW1lIjoic2FucWl5YW54aXNoZUAxNjMuY29tIn0.Y13biw.CUbaB4rLymtkp4F1rkjb47ZQhUw; Expires=Sun, 06 Nov 2022 02:04:55 GMT; HttpOnly; Path=/

## flask session 和 cookie（session的过期时间设置）

https://blog.csdn.net/jzj_c_love/article/details/106167592


## flask g 全局变量

1.什么是g对象。
1.在flask中，有一个专门用来存储用户信息的g对象，g的全称的为global。
2.g对象在一次请求中的所有的代码的地方，都是可以使用的。

2.g对象和session的区别
在我看来，最大的区别是，session对象是可以跨request的，只要session还未失效，不同的request的请求会获取到同一个session，但是g对象不是，g对象不需要管过期时间，请求一次就g对象就改变了一次，或者重新赋值了一次。那么g对象该如何使用呢？看代码。

https://blog.csdn.net/youzhouliu/article/details/88666209


from flask import Flask,jsonify,g


app = Flask(__name__)
count = []


@app.before_request
def before_request():
    print  count


@app.route('/')
def hello_world():
    count.append(1)
    g.count = count
    return 'Hello World!'


@app.route('/get')
def get():
    return jsonify(count=g.count)


if __name__ == '__main__':
    app.run(debug=True)




2022-11-06 

30号

## python bytes -》string

 # bytes object
  b = b"example"
 
  # str object
  s = "example"
 
  # str to bytes
  bytes(s, encoding = "utf8")
 
  # bytes to str
  str(b, encoding = "utf-8")
 
  # an alternative method
  # str to bytes
  str.encode(s)
 
  # bytes to str
  bytes.decode(b)


## session同步

在做了web集群后，你肯定会首先考虑session同步问题，因为通过负载均衡后，同一个IP访问同一个页面会被分配到不同的服务器上，如果不同的服务器用的是不同的reidis服务，那么可能就会出现，一个登录用户，一会是登录状态，一会又不是登录状态。所以session这个时候就要同步了。刚好，我们选择用redis作为了存储，是可以在多台redis 服务器中同步的。

具体可以搜索 reidis主从同步或者redis 集群
————————————————
版权声明：本文为CSDN博主「domorejojo」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/think2me/article/details/38726429

模版提供
flask 框架是基于Jinja2模板引擎实现的
在项目中创建一个子目录templates，然后在其目录下创建demo.html
在flask文件中，应用方法中需要调用
render_template('demo.html', name=name) 复制代码

Flask扩展包：

Flask-SQLalchemy：操作数据库；

Flask-migrate：管理迁移数据库；

Flask-Mail:邮件；

Flask-WTF：表单；

Flask-script：插入脚本；

Flask-Login：认证用户状态；

Flask-RESTful：开发REST API的工具；

Flask-Bootstrap：集成前端Twitter Bootstrap框架；

Flask-Moment：本地化日期和时间；

Flask本身不限定数据库的选择，你可以选择SQL或NOSQL的任何一种。也可以选择更方便的SQLALchemy，类似于Django的ORM。SQLALchemy实际上是对数据库的抽象，让开发者不用直接和数据库打交道，而是通过Python对象来操作数据库，在舍弃一些性能开销的同时，换来的是开发效率的较大提升。

SQLALchemy是一个关系型数据库框架，它提供了高层的ORM和底层的原生数据库的操作。flask-sqlalchemy是一个简化了SQLALchemy操作的flask扩展。

## 参考java的session 

https://blog.csdn.net/Cjava_math/article/details/81563871

https://blog.csdn.net/huangpb123/article/details/103933400


## 任务存储器的意义

任务存储器的选择有两种。一是内存，也是默认的配置。二是数据库。

使用内存的方式是简单高效，但是不好的是，一旦程序出现问题，重新运行的话，会把之前已经执行了的任务重新执行一遍。
数据库则可以在程序崩溃后，重新运行可以从之前中断的地方恢复正常运行。

如果程序启动会重新创建作业，则可以使用默认的内存方式（MemoryJobStore）。如果需要 job 在程序重新启动或崩溃后继续存在，那么建议使用其他 job 存储方式。



有以下几种选择：

MemoryJobStore ：没有序列化，任务存储在内存中，增删改查都是在内存中完成。
SQLAlchemyJobStore ：使用 SQLAlchemy 这个 ORM 框架作为存储方式。
MongoDBJobStore ：使用 mongodb 作为存储器。
RedisJobStore ：使用 redis 作为存储器。
-----------------------------------
©著作权归作者所有：来自51CTO博客作者小呆瓜耶的原创作品，请联系作者获取转载授权，否则将追究法律责任
【Python】任务调度模块APScheduler（内含定点报时案例）
https://blog.51cto.com/xdgy/5611385




任务配置：
设置 coalesce为 False：设置这个目的是，比如由于某个原因导致某个任务积攒了很多次没有执行（比如有一个任务是1分钟跑一次，但是系统原因断了5分钟），如果 coalesce=True，那么下次恢复运行的时候，会只执行一次，而如果设置 coalesce=False，那么就不会合并，会5次全部执行。


max_instances=5：同一个任务同一时间最多只能有5个实例在运行。比如一个耗时10分钟的job，被指定每分钟运行1次，如果我 max_instance值5，那么在第6~10分钟上，新的运行实例不会被执行，因为已经有5个实例在跑了。


## APScheduler不完全踩坑指南

https://juejin.cn/post/7034701720840372261

[测试平台系列(82) 解决APScheduler重复执行的问题 ](https://www.cnblogs.com/we8fans/p/15602505.html)



[分布式定时任务的重复执行问题](https://www.kawabangga.com/posts/2903)



## 

[job_defaults](https://blog.csdn.net/RoninYang/article/details/121131548)



问题
在一个python web应用中需要定时执行一些任务，所以用了APScheduler这个库。又因为是用flask这个web框架，所以用了flask-apscheduler这个插件（本质上与直接用APScheduler一样，这里不作区分）。
在开发中直接测试运行是没有问题的，但是用gunicorn部署以后发生了重复运行的问题：
每个任务在时间到的时刻会同时执行好几遍。
注意了一下重复的数量，恰恰是gunicorn里配置的worker进程数量，显然是每个worker进程都启动了一份scheduler造成。
解决
可以想到的方案有几个：
用–preload启动gunicorn，确保schedu