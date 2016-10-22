from django.db import models

from django.contrib.auth.models import AbstractUser

class Account(AbstractUser, models.Model):
    username = models.CharField(max_length=30, unique=True)
    USERNAME_FIELD = 'username'
