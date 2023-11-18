from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.executors.pool import ThreadPoolExecutor
import time



mongo= MongoClient("localhost",27017)

job_stores = {
       'default': MongoDBJobStore(database="logs",client=mongo,collection="schedulejob")
   }



executors = {
       'default': {'type': 'threadpool', 'max_workers': 60}
   }


job_defaults = {
       'coalesce': True,  # When the same task is triggered multiple times at the same time, it runs only once
       'max_instances': 3,
       'misfire_grace_time': 30,  # The task is still executed after 30 seconds of expiration
}

def my_job(a,b):
    print(a)
    print(b)


sched = BackgroundScheduler(jobstores=job_stores, executors=executors, job_defaults=job_defaults, daemon=True)
sched.add_job(syncdata, 'interval', minutes=5, kwargs={"subdomain": "d3v-digite", "emailid": "sp"},
              name="incrementaljob")
sched.add_listener(listen, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
sched.start()