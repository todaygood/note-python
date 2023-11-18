import threading
import time
from flask import Flask
app = Flask(__name__)

# app.before_request etc
@app.before_first_request
def activate_job():
    def run_job():
        while True:
            print("执行后台任务...")
            time.sleep(3)

    thread = threading.Thread(target=run_job)
    thread.start()

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()