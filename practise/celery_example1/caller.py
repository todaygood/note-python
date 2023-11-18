# -*- coding: utf-8 -*-

from celery_task2 import add

# 异步任务


result = add.delay(4, 4)


print('hello world,result={}'.format(result.get(timeout=7)))

