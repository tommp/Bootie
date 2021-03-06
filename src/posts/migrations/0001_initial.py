# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('category', models.CharField(default=b'news', choices=[(b'news', b'News article'), (b'info_general', b'General information'), (b'info_activity', b'Activity information')], max_length=100, blank=True, null=True, verbose_name=b'category')),
                ('image_description', models.TextField(null=True, blank=True)),
                ('headline', models.CharField(max_length=50, verbose_name=b'headline')),
                ('lead', models.CharField(max_length=100, verbose_name=b'lead', blank=True)),
                ('body', models.TextField(verbose_name=b'body', blank=True)),
                ('authors', models.ManyToManyField(related_name='posts_article_authors', verbose_name=b'authors', to=settings.AUTH_USER_MODEL, blank=True)),
                ('image', models.ForeignKey(blank=True, to='galleries.Image', null=True)),
            ],
        ),
    ]
