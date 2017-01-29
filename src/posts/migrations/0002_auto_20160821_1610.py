# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(default=b'news', choices=[(b'news', b'News article'), (b'info_general', b'General information'), (b'info_activity', b'Activity information'), (b'info_general_english', b'General information in english'), (b'info_activity_english', b'Activity information in english')], max_length=100, blank=True, null=True, verbose_name=b'category'),
        ),
    ]
