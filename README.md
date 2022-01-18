cyclemill
=========

Celery is a good task queue for Django (much better than rolling
you own, am I right) but by default there's no visibilty into it.

There's a tool called flower that monitors celery tasks, and it
used to draw graphs, but it doesn't anymore.  It recommends
Prometheus for this purpose.

This docker-compose stack is a rough demo of setting up a simple Celery
queue on a Django webapp, with some efforts to increase visibility:

*   a Prometheus instance
*   an exporter to provide Celery metrics to Prometheus,
    based on [danihodovic/celery-exporter](https://github.com/danihodovic/celery-exporter/).
*   a Django model (Workflow) that can be displayed to
    show the progress of tasks in Django's views.
*   `django-celery-results` so the results of the tasks are also
    visible in Django's admin interface.

Usage
-----

To bring up the stack:

    docker-compose up

You can then go to

    localhost:8000

where you will have a button that launches celery tasks.  After
launching one, you'll see its status in the Django view.  You
can go to

    localhost:9090

and enter some metrics names to have Prometheus graph the
activity.

You can also go to the Django admin

    localhost:8000/admin

and see the celery results as a table.  To log in, you'll
first probably want to create a superuser to use the admin:

    ./script/manage.py.sh createsuperuser

That's a script that runs the `manage.py` inside the container,
which can be super useful for troubleshooting, especially

    ./script/manage.py.sh shell

Back on the host, you can run

    docker-compose build

to rebuild the images after making changes.  Also handy is

    docker-compose restart worker

(because it doesn't restart by itself when you change the code).

TODO
----

### Task/workflow infrastructure

*   make the workflow task pattern a pattern (decorator?)
*   run a celery "canvas"
*   Chain of tasks, use for workflow decoy
*   Error handling, test thoroughly 

### Django niceties

*   base template
*   unit tests (test the tasks using CELERY_EAGER)
*   form to take length task should run

### Docker niceties

*   don't run Django as root in the container

### Aspirational

*   API endpoints for workflows
*   react app to use API, display the workflow status
