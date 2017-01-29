# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrontpageContext',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('top_logo', models.ForeignKey(blank=True, to='galleries.Image', null=True)),
            ],
            options={
                'verbose_name': 'frontpage_context',
                'verbose_name_plural': 'frontpage_contexts',
            },
        ),
    ]
