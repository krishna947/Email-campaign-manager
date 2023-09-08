from django.contrib import admin
from django.urls import path
from email_app.views import AddSubscriberView, UnsubscribeView

urlpatterns = [
    path('subscribe/', AddSubscriberView.as_view(), name='subscriber'),
    path('unsubscribe/', UnsubscribeView.as_view(), name='unsubscribe'),
    # path('send_daily_campaign/', SendDailyCampaignView.as_view(), name='send_daily_campaign'),
]