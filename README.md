cyclemill
=========

Celery is a good task queue for Django (much better than rolling
your own, am I right) but by default there's no visibilty into it.

There's a tool called [flower](https://flower.readthedocs.io/en/latest/index.html)
that monitors celery tasks, but last I looked at it, it doesn't
draw graphs anymore; instead, it recommended Prometheus for this purpose.
(This may have changed since then.)

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

And for running unit tests, with

    ./script/manage.py.sh test

Back on the host, you can run

    docker-compose build

to rebuild the images after making changes.  Also handy is

    docker-compose restart worker

(because it doesn't restart by itself when you change the code).

TODO
----

### Task/workflow infrastructure

*   Workflow task factory; return a chain of tasks where the first
    creates a workflow, the middle ones (provided by caller) take
    the workflow, and the final one updates the workflow to finished
    state.
*   Show that we can run a celery "canvas" in this pattern.
*   Error handling should update workflow to "failed" state should
    an error occur anywhere in the canvas.  Test this thoroughly.

### Django niceties

*   base template
*   form to take length task should run

### Docker niceties

*   don't run Django as root in the container

### Aspirational

*   measure test coverage
*   API endpoints for workflows
*   react app to use API, display the workflow status
