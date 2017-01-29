# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0001_initial'),
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='frontpagecontext',
            options={'verbose_name': 'frontpage context', 'verbose_name_plural': 'frontpage contexts'},
        ),
        migrations.AddField(
            model_name='frontpagecontext',
            name='facebookImage',
            field=models.ForeignKey(related_name='face_image', blank=True, to='galleries.Image', null=True),
        ),
        migrations.AlterField(
            model_name='frontpagecontext',
            name='top_logo',
            field=models.ForeignKey(related_name='top_logo', blank=True, to='galleries.Image', null=True),
        ),
    ]
