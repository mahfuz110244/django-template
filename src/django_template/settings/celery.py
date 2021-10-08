import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_template.settings')

celery_app = Celery('django_template')

celery_app.config_from_object('django.conf:settings', namespace='CELERY')

celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@celery_app.task(bind=True)
def debug_task(self):
    print(f'Debug Task: {self.request!r}')
