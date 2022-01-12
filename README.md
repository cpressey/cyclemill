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

*   model: workflow (task id, status)
*   PATTERN: have "every" task update its "workflow status" record when it starts
*   PATTERN: have "every" final task update its "workflow status" record when it finishes
*   PATTERN: run a "canvas"
*   form to take length task should run
*   prometheus instance
*   logging
*   research django-celery-results.  how to use its tables?
*   `website` -> `webapp`

### Nice to have

*   web wait for db to be ready
*   run celery worker as non-root to suppress its whining
