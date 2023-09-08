from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'email_service.settings')

# app = Celery('config', broker='amqp://guest:guest@interview_rabbitmq:5672//', include=['interview.task'])
app = Celery('email_service', broker=settings.BROKER_URL)
app.config_from_object('django.conf:settings', namespace='CELERY')

# app.autodiscover_tasks()
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print("Hello from celery")

from celery import shared_task


@shared_task
def sum():
    return "Hello..."