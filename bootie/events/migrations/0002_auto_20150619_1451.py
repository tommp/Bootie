# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-name'], 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='event',
            name='number_of_attendees',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='event',
            name='max_attendees',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='event',
            name='registered_users',
            field=models.ManyToManyField(to='paddleusers.PaddleUser', blank=True),
        ),
    ]
