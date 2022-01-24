import logging
from time import sleep

from webapp import celery_app


logger = logging.getLogger(__name__)


@celery_app.task(bind=True)
def sample_task(self, workflow_id, arg):
    sleep(arg)
    return workflow_id
