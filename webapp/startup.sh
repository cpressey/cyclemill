#!/bin/sh

if [ "x$DJANGO_ROLE" = "xworker" ]; then
  su celery --command="celery -A webapp worker -l INFO"
else
  python manage.py migrate
  python manage.py runserver web:8000
fi
