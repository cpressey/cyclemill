from django.test import TestCase
from django.utils import timezone

from workflow.models import Workflow, WorkflowTask


class WorkflowTests(TestCase):

    def test_workflow_task_relationship(self):
        wf = Workflow.objects.create(
            started_at=timezone.now(),
        )
        self.assertEqual(wf.status, 'RUNNING')
        wft = WorkflowTask.objects.create(
            workflow=wf,
            task_id='12345',
            started_at=timezone.now(),
        )
        self.assertEqual([wft.task_id for wft in wf.tasks.all()], [
            '12345',
        ])
