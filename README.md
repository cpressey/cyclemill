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

    docker-compose restart worker

(because it doesn't restart by itself when you change the code).

TODO
----

*   base template
*   make the workflow task pattern a pattern (decorator?)
*   run a celery "canvas"
*   Chain of tasks, use for workflow decoy
*   Error handling, test thoroughly 
*   form to take length task should run
*   config exporter log level INFO not debug
*   some unit tests, too, why not

### Big

*   API endpoints for workflows
*   react app to use API, display the workflow status
