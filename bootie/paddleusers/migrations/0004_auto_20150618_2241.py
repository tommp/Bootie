# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paddleusers', '0003_auto_20150618_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='icon',
            field=models.ImageField(upload_to=b'images/', null=True, verbose_name=b'Position icon', blank=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='priority',
            field=models.PositiveIntegerField(default=0, help_text=b'The position with the lowest priority will appear first in the frontend column.', verbose_name=b'priority'),
        ),
    ]
