from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render

from django_celery_results.models import TaskResult

from home.tasks import sample_task


def home(request):
    return render(request, 'home.html', {
        'task_results': TaskResult.objects.all().order_by('date_done')
    })


@require_POST
def launch(request):
    sample_task.delay(123)
    return HttpResponse("<h1>Spawned</h1>", content_type="text/html")
