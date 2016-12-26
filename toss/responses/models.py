from conversations.models import Conversation

from django.db import models
from django.conf import settings

class Response(models.Model):
    attending = models.BooleanField(default=True)
    account = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='username', on_delete=models.CASCADE, related_name='responses', null=False)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='responses', null=False)
    
