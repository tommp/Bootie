# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('galleries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'ad name')),
                ('priority', models.FloatField(default=0, verbose_name=b'priority')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated')),
                ('is_published', models.BooleanField(default=False, help_text=b'If this is checked, the ad is visible in the frontend', verbose_name=b'is published')),
                ('url', models.CharField(max_length=200, verbose_name=b'link name')),
                ('authors', models.ManyToManyField(related_name='ads_ad_authors', verbose_name=b'authors', to=settings.AUTH_USER_MODEL, blank=True)),
                ('image', models.ForeignKey(blank=True, to='galleries.Image', null=True)),
            ],
        ),
    ]
