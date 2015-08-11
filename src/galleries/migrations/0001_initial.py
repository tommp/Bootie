# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('is_published', models.BooleanField(default=False, help_text='Approve this content to be published', verbose_name='is published')),
                ('public_from', models.DateTimeField(help_text='The date at which the object will be published (still requires "is published" to be ticked)', null=True, verbose_name='public from')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'gallery',
                'verbose_name_plural': 'galleries',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'images/', max_length=255, verbose_name='image')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('credit_external', models.CharField(max_length=255, verbose_name='credit external person', blank=True)),
                ('image_type', models.CharField(max_length=255, choices=[(b'photo', 'photo'), (b'illustration', 'illustration')])),
                ('credit_user', models.ForeignKey(verbose_name='credit user', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('gallery', models.ForeignKey(related_name='images', verbose_name='gallery', blank=True, to='galleries.Gallery', null=True)),
            ],
            options={
                'ordering': ('-updated',),
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
            },
        ),
    ]
