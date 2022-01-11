from django.http import HttpResponse
from django.views.decorators.http import require_POST

from home.tasks import sample_task


def home(request):
    return HttpResponse("<h1>It works!</h1>", content_type="text/html")



# @require_POST
def launch(request):
    sample_task.delay(123)
    return HttpResponse("<h1>Spawned</h1>", content_type="text/html")
