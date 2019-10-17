from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from app.fenixapp.models import MomoRequest
from app.fenixapp.momoapi_client import collection_client


# default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
app = Celery('app')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


momo_request = MomoRequest()


@periodic_task(
    run_every=(crontab(minute='*/60')),
    name="task to check transaction request status",
    ignore_result=True
)
def check_transaction_request_status():
    """
    Task checks for the status of pending payments and updates the momorequest
    """
    pending_requests = MomoRequest.objects.all().filter(request_status='PENDING')
    for request in pending_requests:
        get_status = collection_client.getTransactionStatus(
            transaction_id=pending_requests.transaction_ref)
        if get_status['status'] == 'SUCCESSFUL':
            momo_request.request_status = get_status['status']
            momo_request.save()
