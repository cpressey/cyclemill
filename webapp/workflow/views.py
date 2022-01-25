from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.http import require_POST

from workflow.forms import LaunchWorkflowForm
from workflow.models import Workflow
from workflow.tasks import signature_simple, signature_chain
from workflow.workflows import start_workflow_canvas


def home(request):
    return render(request, 'home.html', {
        'workflows': Workflow.objects.all().order_by('-started_at').prefetch_related('tasks'),
        'form': LaunchWorkflowForm(),
    })


@require_POST
def launch(request):
    # TODO parse with LaunchWorkflowForm here, instead of this manual stuff

    type, signature = {
        'simple': ('Simple', signature_simple),
        'chain': ('Chain', signature_chain),
    }[request.POST.get('type')]

    duration = request.POST.get('duration')
    try:
        duration = int(duration)
    except ValueError:
        return HttpResponseBadRequest()

    workflow = start_workflow_canvas(type, signature(duration))
    messages.info(request, '[Workflow {}] is now {} (duration: {} seconds).'.format(
        workflow.id, workflow.status, duration
    ))
    return HttpResponseRedirect('/')
