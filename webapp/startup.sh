#!/bin/sh

wait-for-it db:5432
wait-for-it queue:5672
if [ "x$DJANGO_ROLE" = "xworker" ]; then
  celery -A webapp worker -l INFO
else
  python manage.py migrate
  python manage.py runserver web:8000
fi
