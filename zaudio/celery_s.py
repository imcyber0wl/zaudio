from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','zaudio.settings')
#instead of proj put your project name

app=Celery('zaudio')
app.config_from_object('django.conf:settings',namespace='CELERY')
app.autodiscover_tasks() #discover tasks in our application
