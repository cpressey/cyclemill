import logging
from time import sleep

from django.utils import timezone

from webapp import celery_app

from workflow.models import Workflow, WorkflowTask


logger = logging.getLogger(__name__)


@celery_app.task(bind=True)
def sample_task(self, workflow_id, arg):
    now = timezone.now()
    workflow = Workflow.objects.get(id=workflow_id)
    workflow_task = WorkflowTask.objects.create(workflow=workflow, task_id=self.request.id, started_at=now)
    logger.info('Starting [{}] for [Workflow {}]...'.format(workflow_task, workflow.id))
    sleep(arg)
    workflow.status = 'COMPLETED'
    workflow.save()
    logger.info('[Workflow {}] is now {}'.format(workflow.id, workflow.status))
    return arg
