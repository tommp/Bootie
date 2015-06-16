# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PaddleUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Created')),
                ('paid_until', models.DateTimeField(verbose_name=b'Equipment rental valid until')),
                ('profile_pic', models.ImageField(upload_to=b'images/', null=True, verbose_name=b'Profile picture', blank=True)),
                ('banned', models.BooleanField(default=False, help_text=b'If this is checked, the user is banned and can no longer sign up for events and will not recieve the code for skansen.', verbose_name=b'Banned')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Board position')),
                ('user', models.ForeignKey(to='paddleusers.PaddleUser', blank=True)),
            ],
        ),
    ]
