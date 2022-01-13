from time import sleep

from webapp import celery_app

@celery_app.task(bind=True)
def sample_task(self, arg):
    sleep(60)
    print(arg)
    return arg
