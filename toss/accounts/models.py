from django.db import models

from django.contrib.auth.models import AbstractUser

class Account(AbstractUser, models.Model):
    username = models.CharField(max_length=30, unique=True)
    USERNAME_FIELD = 'username'

    email = models.EmailField(max_length=60, blank=False, unique=True)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)

import accounts.signals
