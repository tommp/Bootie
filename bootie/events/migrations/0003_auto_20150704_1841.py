# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paddleusers', '0005_auto_20150704_1841'),
        ('events', '0002_auto_20150619_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventRegistrar',
            fields=[
                ('car_seats', models.IntegerField(default=0)),
                ('paddle_user', models.OneToOneField(primary_key=True, serialize=False, to='paddleusers.PaddleUser')),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='registered_users',
            field=models.ManyToManyField(to='events.EventRegistrar', blank=True),
        ),
    ]
