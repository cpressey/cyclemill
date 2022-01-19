#!/bin/sh

docker-compose exec --user $(id -u):$(id -g) web \
    coverage run manage.py test -v 2
docker-compose exec --user $(id -u):$(id -g) web \
    coverage html
sensible-browser webapp/htmlcov/index.html
