from celery import Celery


app = Celery('task', backend='redis://localhost', broker='redis://localhost')

@app.task
def add(x, y):
    return x + y