from django.contrib import admin
from workflow.models import Workflow, WorkflowTask


admin.site.register(Workflow)
admin.site.register(WorkflowTask)
