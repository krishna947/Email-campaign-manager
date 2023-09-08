from django.contrib import admin
from email_app.models import Subscriber, Campaign

admin.site.register(Subscriber)
admin.site.register(Campaign)