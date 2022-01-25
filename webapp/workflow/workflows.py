import logging

from django.utils import timezone

from webapp import celery_app
from workflow.models import Workflow, WorkflowTask


logger = logging.getLogger(__name__)


def start_workflow_canvas(signature):
    """The supplied `signature` should be the signature of a task that takes a
    workflow ID as its first argument (all other arguments to the task must be
    included in the supplied signature), and returns that same workflow ID
    as its result."""
    now = timezone.now()
    workflow = Workflow.objects.create(type='Basic', started_at=now)
    logger.info('[Workflow {}] is now {}'.format(workflow.id, workflow.status))
    (signature | workflow_finalizer_task.s()).delay(workflow.id)
    return workflow


@celery_app.task(bind=True)
def workflow_finalizer_task(self, workflow_id):
    workflow = Workflow.objects.get(id=workflow_id)
    workflow.status = 'COMPLETED'
    workflow.save()
    logger.info('[Workflow {}] is now {}'.format(workflow.id, workflow.status))
    return workflow_id


def workflow_task(callable):
    """Decorator for making "workflow tasks", which are Celery tasks
    that can be used with the Workflow/WorkflowTask system.
    """

    def wrapper(task, workflow_id, *args, **kwargs):
        now = timezone.now()
        workflow_task = WorkflowTask.objects.create(workflow_id=workflow_id, task_id=task.request.id, started_at=now)
        logger.info('Starting task for [Workflow {}]...'.format(workflow_id))
        task.workflow_id = workflow_id
        callable(task, *args, **kwargs)
        workflow_task.completed_at = timezone.now()
        workflow_task.save()
        return workflow_id
    return wrapper
