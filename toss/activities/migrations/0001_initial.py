# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 03:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conversations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16)),
                ('date', models.DateTimeField()),
                ('location', models.CharField(max_length=30)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to=settings.AUTH_USER_MODEL, to_field='username')),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='conversations.Conversation')),
            ],
        ),
    ]