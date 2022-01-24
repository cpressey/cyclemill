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
    (workflow_initializer_task.s() | signature | workflow_finalizer_task.s()).delay(workflow.id)
    return workflow


@celery_app.task(bind=True)
def workflow_initializer_task(self, workflow_id):
    now = timezone.now()
    workflow = Workflow.objects.get(id=workflow_id)
    # FIXME: how is this going to work now? The request.id is specific to this task, not the chain!
    workflow_task = WorkflowTask.objects.create(workflow=workflow, task_id=self.request.id, started_at=now)
    logger.info('Starting [{}] for [Workflow {}]...'.format(workflow_task, workflow.id))
    return workflow_id


@celery_app.task(bind=True)
def workflow_finalizer_task(self, workflow_id):
    workflow = Workflow.objects.get(id=workflow_id)
    workflow.status = 'COMPLETED'
    workflow.save()
    logger.info('[Workflow {}] is now {}'.format(workflow.id, workflow.status))
    return workflow_id
