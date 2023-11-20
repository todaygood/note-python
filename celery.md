
## celery 入门

https://blog.csdn.net/youzhouliu/article/details/124239709



## celery 分布式部署

https://blog.csdn.net/weixin_55551408/article/details/115404082?spm=1001.2101.3001.6650.4&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EESLANDING%7Edefault-4-115404082-blog-124239709.pc_relevant_landingrelevant&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EESLANDING%7Edefault-4-115404082-blog-124239709.pc_relevant_landingrelevant&utm_relevant_index=5

celery作为分布式的任务队列框架，worker是可以执行在不同的服务器上的。部署过程和单机上启动是一样。只要把项目代码copy到其他服务器，使用相同命令就可以了。可以思考下，这个是怎么实现的？对了，就是通过共享Broker队列。

使用合适的队列，如redis，单进程单线程的方式可以有效地避免同个任务被不同worker同时执行的情况。


celery作为支持分布式，理论上可以无限扩展worker。默认情况下celery提交任务后，任务会放入名为celery的队列，所有在线的worker都会从任务队列中获取任务，任一个worker都有可能执行这个任务。有时候，有时候任务的特殊性或者机器本身的限制，某些任务只能跑在某些worker上。celery提供了queue在区别不同的worker，很好地支持这种情况。

启动worker时，-Q 指定worker支持的任务列队名, 可以支持多个队列名哦
celery worker -A wedo  -l debug -c 4 -Q celery,hipri

任务调用时， queue=*来指定需要执行worker
result = mul.apply_async(args=(2, 2), queue='hipri')


任务队列监控
如果你想通过可视化的方式，查看celery的一切。flower提供可行的解决方案，十分的方便



## celery + supervisor + 阿里云短信，简单实现天气订阅

https://zhuanlan.zhihu.com/p/471477152

