from time import sleep

from website import celery_app

@celery_app.task(bind=True)
def sample_task(self, arg):
    sleep(60)
    print(arg)
    return arg
