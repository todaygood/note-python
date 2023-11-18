#!/bin/bash


echo "begin celery worker..."

celery  -A  worker2  worker  


# celery --app=proj worker -l INFO 
#
# celery -A proj worker -l INFO -Q hipri,lopri 
#
# celery -A proj worker --concurrency=4 
#
# celery -A proj worker --concurrency=1000 -P eventlet 
#
# celery worker --autoscale=10,0



