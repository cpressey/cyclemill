from django.db import models


class Workflow(models.Model):
    STATUSES = (
        ('RUNNING', 'Running'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
    )
    type = models.CharField(max_length=60)
    started_at = models.DateTimeField()
    status = models.CharField(max_length=60, choices=STATUSES, default='RUNNING')


class WorkflowTask(models.Model):
    """
    Although this is set up like a many-to-many relationship
    between Workflows and TaskResults, in practice, each TaskResult
    is only ever associated with one Workflow.  (I just don't want to change the
    TaskResult model to put the ForeignKey in it.)
    """
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE)
    task_id = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Task ID',
        help_text='Celery ID for the Task that was run'
    )
    started_at = models.DateTimeField()
    task_result = models.ForeignKey('django_celery_results.TaskResult', null=True, on_delete=models.CASCADE)
