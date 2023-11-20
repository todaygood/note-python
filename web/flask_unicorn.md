


# equivalent to 'from hello import app'
$ gunicorn -w 4 'hello:app'

# equivalent to 'from hello import create_app; create_app()'
$ gunicorn -w 4 'hello:create_app()'

Starting gunicorn 20.1.0
Listening at: http://127.0.0.1:8000 (x)
Using worker: sync
Booting worker with pid: x
Booting worker with pid: x
Booting worker with pid: x
Booting worker with pid: x


