RottenMQ
========

To build the image and bring up the stack:

    docker-compose build
    docker-compose up

To "telnet" into the container as root (to e.g. install things):

    docker-compose exec web bash

To "telnet" into the container as regular user (to e.g. run `manage.py`):

    docker-compose exec --user $(id -u):$(id -g) web bash

TODO
----

a basic app
urlpatterns to that app
sample task, launch task
django-rest-framework
