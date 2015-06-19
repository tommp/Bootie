# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paddleusers', '0002_position_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='description',
            field=models.TextField(default=b'A member of the board, beautiful and glorious. Sexy and skilled beyond measure.', verbose_name=b'position description'),
        ),
        migrations.AlterField(
            model_name='position',
            name='priority',
            field=models.PositiveIntegerField(default=0, verbose_name=b'priority'),
        ),
    ]
