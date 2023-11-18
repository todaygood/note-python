# coding=utf-8

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


def timed_task():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == '__main__':
    # 创建当前线程执行的schedulers
    scheduler = BlockingScheduler()
    # 添加调度任务(timed_task),触发器选择interval(间隔性),间隔时长为5秒
    scheduler.add_job(timed_task, 'interval', seconds=5)
    # 启动调度任务
    scheduler.start()

"""
————————————————
版权声明：本文为CSDN博主「那些年踩过的坑丶」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_22034353/article/details/89362959
"""
