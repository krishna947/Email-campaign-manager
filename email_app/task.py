from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from email_app.models import Subscriber, Campaign
from django.forms.models import model_to_dict


@shared_task()
def add(x, y):
    return x + y


@shared_task
def send_email(email_id, campaign_data):
    return "Email sent successfully"


def send_daily_email_campaign():
    campaign = Campaign.objects.get(id=1)
    print(campaign)
    obj_dict = model_to_dict(campaign)
    subscribers = Subscriber.objects.filter(is_active=True)
    print(subscribers.count())
    for subscriber in subscribers:
        send_email.delay(subscriber.email_id, obj_dict)
    print("mmmmm")