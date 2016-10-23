from django.db import models
from django.conf import settings

class Conversation(models.Model):
    members = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='conversations', null=False)
