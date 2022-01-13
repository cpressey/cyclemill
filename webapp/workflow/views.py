from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.shortcuts import render

#from django_celery_results.models import TaskResult

from workflow.models import Workflow, WorkflowTask
from workflow.workflows import start_basic_workflow


def home(request):
    return render(request, 'home.html', {
        'workflows': Workflow.objects.all().order_by('started_at')
    })


@require_POST
def launch(request):
    start_basic_workflow(30)
    # django.messages
    return HttpResponseRedirect('/')
