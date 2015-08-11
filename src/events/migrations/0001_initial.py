# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paddleusers', '__first__'),
        ('posts', '__first__'),
        ('galleries', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'category')),
                ('image', models.ForeignKey(to='galleries.Image', null=True)),
            ],
            options={
                'ordering': ['-name'],
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
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
                ('image_description', models.TextField(null=True, blank=True)),
                ('max_attendees', models.IntegerField(default=0, help_text=b'Leave at 0 to disable registration')),
                ('number_of_attendees', models.IntegerField(default=0)),
                ('cost', models.IntegerField(default=0)),
                ('show_attendees', models.BooleanField(default=True, verbose_name=b'Show attendees')),
                ('category', models.ManyToManyField(to='events.Category')),
                ('event_article', models.ForeignKey(to='posts.Article')),
                ('image', models.ForeignKey(blank=True, to='galleries.Image', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventRegistrar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('car_seats', models.IntegerField(default=0)),
                ('event', models.ForeignKey(to='events.Event')),
                ('paddle_user', models.ForeignKey(to='paddleusers.PaddleUser')),
            ],
        ),
    ]
