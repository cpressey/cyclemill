import logging
from django.utils import timezone

from workflow.models import Workflow
from workflow.tasks import sample_task


logger = logging.getLogger(__name__)


def start_basic_workflow(arg):
    now = timezone.now()
    workflow = Workflow.objects.create(type='Basic', started_at=now)
    logger.info('[Workflow {}] is now {}'.format(workflow.id, workflow.status))
    sample_task.delay(workflow.id, arg)
    return workflow
