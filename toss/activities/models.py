from accounts.models import Account

from django.db import models
from django.conf import settings

class Activity(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='username', on_delete=models.CASCADE, related_name='activities', null=False)
    title = models.CharField(max_length=16, blank=False)
    date = models.DateTimeField(null=False)
    location = models.CharField(max_length=30, blank=False)
