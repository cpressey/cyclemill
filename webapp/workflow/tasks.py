from time import sleep

from django.utils import timezone

from webapp import celery_app


def start_basic_workflow(arg):
    from workflow.models import Workflow, WorkflowTask
    now = timezone.now()
    workflow = Workflow.objects.create(type='Basic', started_at=now)
    sample_task.delay(workflow.id, arg)


@celery_app.task(bind=True)
def sample_task(self, workflow_id, arg):
    now = timezone.now()
    workflow = Workflow.objects.get(id=workflow_id)
    workflow_task = WorkflowTask.objects.create(workflow=workflow, task_uuid='', started_at=now)
    sleep(arg)
    workflow.status = 'COMPLETED'
    workflow.save()
    return arg
