# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated')),
                ('is_published', models.BooleanField(default=False, help_text=b'If this is checked, the article is visible in the frontend', verbose_name=b'is published')),
                ('slug', models.SlugField(unique=True, max_length=200, verbose_name=b'slug', blank=True)),
                ('category', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'category', choices=[(b'info', b'Information archive'), (b'news', b'News article')])),
                ('image', models.ImageField(upload_to=b'', null=True, verbose_name=b'image', blank=True)),
                ('image_description', models.TextField(null=True, blank=True)),
                ('headline', models.CharField(max_length=100, verbose_name=b'headline')),
                ('body', models.TextField(verbose_name=b'body', blank=True)),
            ],
        ),
    ]
