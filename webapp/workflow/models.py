from django.db import models

# from django_celery_results.models import TaskResult


class Workflow(models.Model):
    work_name = models.CharField(max_length=60)
    started_at = models.DateTimeField()


class WorkflowTask(models.Model):
    """
    Although this is set up like a many-to-many relationship
    between Workflows and TaskResults, in practice, one TaskResult
    is only ever in one Workflow.  (I just don't want to change the
    TaskResult model to put the ForeignKey in it.)
    """
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE)
    task = models.ForeignKey('django_celery_results.TaskResult', on_delete=models.CASCADE)
