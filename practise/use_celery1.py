

from celery import Celery

app = Celery('hello', broker='amqp://hujun1:todayGood123@pcentos.hujun.com:5672/hujunhost1')

@app.task
def hello():
    return 'hello world'


"""
https://hub.docker.com/_/rabbitmq/

pip install "celery[librabbitmq,redis,auth,msgpack]"

https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html#broker-rabbitmq

$ sudo rabbitmqctl add_user myuser mypassword
$ sudo rabbitmqctl add_vhost myvhost
$ sudo rabbitmqctl set_user_tags myuser mytag
$ sudo rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"




组件介绍：

Producer：调用了Celery提供的API、函数或者装饰器而产生任务并交给任务队列处理的都是任务生产者。
Celery Beat：任务调度器，Beat进程会读取配置文件的内容，周期性地将配置中到期需要执行的任务发送给任务队列。
Broker：消息代理，又称消息中间件，接受任务生产者发送过来的任务消息，存进队列再按序分发给任务消费方（通常是消息队列或者数据库）。Celery目前支持RabbitMQ、Redis、MongoDB、Beanstalk、SQLAlchemy、Zookeeper等作为消息代理，但适用于生产环境的只有RabbitMQ和Redis, 官方推荐 RabbitMQ。
Celery Worker：执行任务的消费者，通常会在多台服务器运行多个消费者来提高执行效率。
Result Backend：任务处理完后保存状态信息和结果，以供查询。Celery默认已支持Redis、RabbitMQ、MongoDB、Django ORM、SQLAlchemy等方式。
  在客户端和消费者之间传输数据需要序列化和反序列化。
————————————————
版权声明：本文为CSDN博主「LQ_2021」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/LelemamaAnne/article/details/115700490


https://docs.celeryq.dev/en/stable/userguide/application.html

"""