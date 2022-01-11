from website import celery_app

@celery_app.task(bind=True)
def sample_task(self, arg):
    print(arg)
    return arg
