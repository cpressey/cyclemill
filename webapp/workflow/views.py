from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.http import require_POST

from workflow.forms import LaunchTaskForm
from workflow.models import Workflow, WorkflowTask
from workflow.workflows import start_basic_workflow


def home(request):
    return render(request, 'home.html', {
        'workflows': Workflow.objects.all().order_by('started_at'),
        'form': LaunchTaskForm(),
    })


@require_POST
def launch(request):
    duration = request.POST.get('duration')
    try:
        duration = int(duration)
    except ValueError:
        return HttpResponseBadRequest()
    workflow = start_basic_workflow(duration)
    messages.info(request, '[Workflow {}] is now {} (duration: {} seconds).'.format(
        workflow.id, workflow.status, duration
    ))
    return HttpResponseRedirect('/')
