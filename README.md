cyclemill
=========

**IMPORTANT NOTE**: *This stack is not hardened.  You should not run it in production.*

Overview
--------

Celery is a good task queue for Django (much better than rolling
your own, am I right) but by default there's no visibilty into it.

There's a tool called [flower](https://flower.readthedocs.io/)
that monitors celery tasks, but last I looked at it, it doesn't
draw graphs anymore; instead, it recommended [Prometheus](https://prometheus.io/) for this purpose.
(This may have changed since then.)

**cyclemill** is a docker-compose stack that demonstrates setting up a simple Celery
queue on a Django webapp, with some efforts to increase visibility:

*   a Prometheus instance;
*   an exporter to provide Celery metrics to Prometheus,
    based on [danihodovic/celery-exporter](https://github.com/danihodovic/celery-exporter/);
*   a Django model (Workflow) that can be displayed to
    show the progress of tasks in Django's views; and
*   [django-celery-results](https://django-celery-results.readthedocs.io/) so the results of the tasks are also
    visible in Django's admin interface.

(That last feature is possibly superfluous.  Task results are more of an
implementation detail of Celery.  The value of being able to view them in the admin
is debatable, and having them in Redis would be more efficient.)

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

Development
-----------

The webapp and worker containers have bind mounts on the
`webapp` directory.  So any time you edit files under
`webapp`, those changes are seen immediately in the container.

But if you need to rebuild the images for other reasons,
you can run

    docker-compose build

after making changes.  Also handy is

    docker-compose restart worker

because unlike Django, Celery doesn't automatically restart
when you make changes to the source code files.

To run unit tests, you can

    ./script/manage.py.sh test

To run unit tests and also generate a test coverage report,

    ./script/coverage.sh

If you are short on resources you don't have to bring up
every single one of the containers.  A slimmer, but still
functional, set is

    docker-compose up web worker db queue

TODO
----

### Task/workflow infrastructure

*   Decorator or something for the "workflow task" pattern.
*   Demo task that runs subtasks in a group.
*   Demo task that runs subtasks in a chord.
*   Show the tasks of a workflow, in the UI, under each workflow.
*   Error handling should update workflow to "failed" state should
    an error occur anywhere in the canvas.  Test this thoroughly.
*   Can on_error even have access to workflow_id?  Not sure.

### Aspirational

*   API endpoints for workflows
*   react app to use API, display the workflow status, refresh
