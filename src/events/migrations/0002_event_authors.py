# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='authors',
            field=models.ManyToManyField(related_name='events_event_authors', null=True, verbose_name=b'authors', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]