import logging
from django.utils import timezone

from workflow.models import Workflow
from workflow.tasks import sample_task


logger = logging.getLogger(__name__)


def start_workflow_canvas(signature):
    """The supplied `signature` should be the signature of a task that takes a
    workflow ID as its first argument (all other arguments to the task must be
    included in the supplied signature), and returns that same workflow ID
    as its result."""
    now = timezone.now()
    workflow = Workflow.objects.create(type='Basic', started_at=now)
    logger.info('[Workflow {}] is now {}'.format(workflow.id, workflow.status))
    # TODO: signature.link(workflow_final_task.s())
    signature.delay(workflow.id)
    return workflow
