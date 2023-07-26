import os
from celery import Celery,shared_task

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')  # Replace 'demo' with your Django project name.

app = Celery('cicd')  # Replace 'cicd' with the app name containing Celery tasks.

app.conf.broker_connection_retry_on_startup = True
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()