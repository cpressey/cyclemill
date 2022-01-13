from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_POST

from workflow.models import Workflow, WorkflowTask
from workflow.workflows import start_basic_workflow


def home(request):
    return render(request, 'home.html', {
        'workflows': Workflow.objects.all().order_by('started_at')
    })


@require_POST
def launch(request):
    workflow = start_basic_workflow(30)
    messages.info(request, '[Workflow {}] is now {}.'.format(workflow.id, workflow.status))
    return HttpResponseRedirect('/')
