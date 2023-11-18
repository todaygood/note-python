from flask import Flask
from flask_apscheduler import APScheduler
import logging
import time
import threading

app = Flask(__name__)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

log_format = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(stream=open('use_flask_apscheduler1.log', "a+", encoding='utf-8'), level='DEBUG',
                    format=log_format,
                    force=True)  # 这里必须设置force=True

logger = logging.getLogger(__name__)


@app.route('/')
def welcome():
    return 'Welcome to flask_apscheduler demo', 200


def thread_tasks():
    scheduler.add_job(func=scheduled_task, trigger='interval', id='mywork2', minutes=1, args=['mywork2'])

    return True


@app.route('/run-tasks')
def run_tasks():
    scheduler.add_job(func=scheduled_task, trigger='interval', id='mywork1', seconds=5, args=['mywork1'])

    return 'Scheduled several long running tasks.', 200


def scheduled_task(id):
    logger.debug('{} {} Task running '.format(id, time.time()))


thread = threading.Thread(target=thread_tasks)

thread.start()

app.run(host='0.0.0.0', port=12345, debug=False)


"""
执行两遍 

https://www.codenong.com/14874782/

解决 flask_apscheduler 函数执行两次的问题 https://juejin.cn/post/6844903917206110216

"""