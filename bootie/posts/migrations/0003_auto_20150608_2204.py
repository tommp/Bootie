# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_article_lead'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(default=b'news', choices=[(b'news', b'News article'), (b'info_general', b'General information'), (b'info_activity', b'Activity information')], max_length=100, blank=True, null=True, verbose_name=b'category'),
        ),
        migrations.AlterField(
            model_name='article',
            name='headline',
            field=models.CharField(max_length=50, verbose_name=b'headline'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to=b'images/', null=True, verbose_name=b'image', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='lead',
            field=models.CharField(max_length=100, verbose_name=b'lead', blank=True),
        ),
    ]
