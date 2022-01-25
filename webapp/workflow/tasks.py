import logging
from time import sleep

from webapp import celery_app
from workflow.workflows import workflow_task


logger = logging.getLogger(__name__)


@celery_app.task(bind=True)
@workflow_task
def sample_task(self, arg):
    logger.info("This task will now sleep for {} seconds.".format(arg))
    sleep(arg)
