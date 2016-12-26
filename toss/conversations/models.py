from accounts.models import Account

from django.db import models
from django.conf import settings

class Conversation(models.Model):
    members = models.ManyToManyField(Account)
