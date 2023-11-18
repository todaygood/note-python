# -*- coding: utf-8 -*-

import time
from celery import Celery

broker = 'redis://pcentos.hujun.com:6379'
backend = 'redis://pcentos.hujun.com:6379/3'

app = Celery('my_task', broker=broker, backend=backend)


@app.task
def add(x, y):
    time.sleep(5)  # 模拟耗时操作
    return x + y


