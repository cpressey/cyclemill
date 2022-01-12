#!/bin/sh

docker-compose exec --user $(id -u):$(id -g) web python manage.py $*
