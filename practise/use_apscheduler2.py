import time

from flask_apscheduler import APScheduler


def test_scheduler():
    print("TEST")
    print(time.time())


sched = APScheduler()
sched.add_job("test", test_scheduler, trigger='interval', seconds=5)
sched.start()

while True:
    time.sleep(60)
