from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.shortcuts import render

from django_celery_results.models import TaskResult

from workflow.tasks import start_basic_workflow


def home(request):
    return render(request, 'home.html', {
        'task_results': TaskResult.objects.all().order_by('date_done')
    })


@require_POST
def launch(request):
    start_basic_workflow.delay(30)
    # django.messages
    return HttpResponseRedirect('/')
