import logging
from time import sleep

from django.utils import timezone

from webapp import celery_app
from workflow.models import WorkflowTask


logger = logging.getLogger(__name__)


@celery_app.task(bind=True)
def sample_task(self, workflow_id, arg):
    """This is an example of a "workflow task", which must follow these rules:

    - take workflow_id as first argument
    - return the same workflow_id
    - create the WorkflowTask object at the start
    - update the WorkflowTask object at the end

    TODO: write a decorator that does all this for you
    """
    now = timezone.now()
    workflow_task = WorkflowTask.objects.create(workflow_id=workflow_id, task_id=self.request.id, started_at=now)
    logger.info('Starting task for [Workflow {}]...'.format(workflow_id))
    sleep(arg)
    workflow_task.completed_at = timezone.now()
    workflow_task.save()
    return workflow_id
