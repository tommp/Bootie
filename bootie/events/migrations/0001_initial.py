# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        ('paddleusers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'category')),
                ('image', models.ImageField(upload_to=b'images/', null=True, verbose_name=b'image')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'event name')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'updated')),
                ('start_date', models.DateTimeField(verbose_name=b'start time')),
                ('end_date', models.DateTimeField(verbose_name=b'end time')),
                ('registration_open_date', models.DateTimeField(verbose_name=b'registration open time')),
                ('registration_cutoff_date', models.DateTimeField(verbose_name=b'registration cutoff time')),
                ('cancellation_cutoff_date', models.DateTimeField(verbose_name=b'cancellation cutoff time')),
                ('is_published', models.BooleanField(default=False, help_text=b'If this is checked, the event is visible in the frontend', verbose_name=b'is published')),
                ('slug', models.SlugField(unique=True, max_length=200, verbose_name=b'slug')),
                ('image', models.ImageField(upload_to=b'images/', null=True, verbose_name=b'image', blank=True)),
                ('image_description', models.TextField(null=True, blank=True)),
                ('max_attendees', models.IntegerField(default=1)),
                ('cost', models.IntegerField(default=0)),
                ('show_attendees', models.BooleanField(default=True, verbose_name=b'Show attendees')),
                ('category', models.ManyToManyField(to='events.Category')),
                ('event_article', models.ForeignKey(to='posts.Article')),
                ('registered_users', models.ManyToManyField(to='paddleusers.PaddleUser')),
            ],
        ),
    ]
