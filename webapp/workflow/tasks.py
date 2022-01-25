import logging
from time import sleep

from webapp import celery_app
from workflow.workflows import workflow_task


logger = logging.getLogger(__name__)


@celery_app.task(bind=True)
@workflow_task
def sleep_task(self, duration):
    logger.info("This task will now sleep for {} seconds.".format(duration))
    sleep(duration)


def signature_simple(duration):
    return sleep_task.s(duration)


def signature_chain(duration):
    return sleep_task.s(duration / 3) | sleep_task.s(duration / 3) | sleep_task.s(duration / 3)
