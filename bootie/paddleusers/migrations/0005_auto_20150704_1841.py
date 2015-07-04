# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paddleusers', '0004_auto_20150618_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='priority',
            field=models.PositiveIntegerField(default=0, help_text=b'The position with the hoghest priority will appear first in the frontend column.', verbose_name=b'priority'),
        ),
        migrations.AlterField(
            model_name='position',
            name='user',
            field=models.ForeignKey(to='paddleusers.PaddleUser'),
        ),
    ]
