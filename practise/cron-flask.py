"""Advanced example using other configuration options."""

from apscheduler.jobstores.mongodb import MongoDBJobStore
from flask import Flask

from flask_apscheduler import APScheduler


class Config:
    """App configuration.

    JOBS = [
        {
            "id": "job1",
            "func": "advanced:job1",
            "args": (1, 2),
            "trigger": "interval",
            "seconds": 10,
        }
    ]
    """
    SCHEDULER_JOBSTORES = {"default": MongoDBJobStore(host='pcentos.hujun.com', port=27017)}

    SCHEDULER_EXECUTORS = {"default": {"type": "threadpool", "max_workers": 20}}

    SCHEDULER_JOB_DEFAULTS = {"coalesce": False, "max_instances": 3}

    SCHEDULER_API_ENABLED = True


def job1(var_one, var_two):
    """Demo job function.

    :param var_two:
    :param var_two:
    """
    print(str(var_one) + " " + str(var_two))


app = Flask(__name__)

@app.route('/')
def index():
    scheduler.add_job(id="my-job", func=job1,trigger='interval',replace_existing=True, args=(3,5))
    return "hello,world"


if __name__ == "__main__":

    app.config.from_object(Config())

    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()

    app.run(host="0.0.0.0",debug=True)
