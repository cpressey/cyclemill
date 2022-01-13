RottenMQ
========

To build the image and bring up the stack:

    docker-compose build
    docker-compose up

You probably want to create a superuser to use the admin:

    ./script/manage.py.sh createsuperuser

That script runs the `manage.py` inside the container,
which can be super useful for troubleshooting, especially

    ./script/manage.py.sh shell

Back on the host, another handy command is

    docker-compose restart web

TODO
----

*   make the workflow task pattern a pattern (decorator?)
*   run a celery "canvas"
*   make the page refresh
*   form to take length task should run
*   prometheus instance
*   have prometheus monitor celery
*   logging
*   web wait for db to be ready
