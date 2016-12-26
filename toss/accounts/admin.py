from .models import Account

from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

class AccountAdmin(UserAdmin):
    pass

admin.site.register(Account, AccountAdmin)
