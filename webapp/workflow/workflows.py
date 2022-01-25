import logging

from django.utils import timezone

from webapp import celery_app
from workflow.models import Workflow


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
