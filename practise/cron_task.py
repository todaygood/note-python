from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.executors.pool import ThreadPoolExecutor
import time

#scheduler = BlockingScheduler()

executors = {'default': ThreadPoolExecutor(20)}
scheduler = BackgroundScheduler(executors = executors)

print("aaaa....")

def my_job(a,b):
    print("{} {}".format(a,b))
    # 判断是否处于交易状态

    # 获取这个周期内的stock_list


    # 监控价格，告警



# scheduler.add_job(my_job,'date',args=[100,'python'])
scheduler.add_job(my_job,'interval',seconds=3,args=[100,'python'])




scheduler.start()
print("after start...")
while True:
    time.sleep(5)