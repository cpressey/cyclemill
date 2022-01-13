from datetime import datetime
from time import sleep

from webapp import celery_app


def start_basic_workflow(arg):
    from workflow.models import Workflow, WorkflowTask
    workflow = Workflow.objects.create(type='Basic', started_at=datetime.utcnow())
    sample_task.delay(workflow.id, arg)


@celery_app.task(bind=True)
def sample_task(self, workflow_id, arg):
    workflow = Workflow.objects.get(id=workflow_id)
    workflow_task = WorkflowTask.objects.create(workflow=workflow, task_uuid='', started_at=datetime.utcnow())
    sleep(arg)
    return arg
