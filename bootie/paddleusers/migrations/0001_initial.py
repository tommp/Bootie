# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PaddleUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profile_pic', models.ImageField(upload_to=b'images/', null=True, verbose_name=b'profile picture', blank=True)),
                ('position', models.CharField(blank=True, max_length=100, null=True, verbose_name=django.db.models.fields.CharField, choices=[(b'Leder', b'Leder'), (b'Leder', b'Nestleder'), (b'\xc3\x98konomisjef', b'\xc3\x98konomisjef'), (b'Elvesjef', b'Elvesjef'), (b'Havsjef', b'Havsjef'), (b'Websjef', b'Websjef'), (b'Utstyrssjef hav', b'Utstyrssjef hav'), (b'Utstyressjef elv', b'Utstyressjef elv'), (b'Polosjef', b'Polosjef'), (b'Websjef', b'Websjef'), (b'Sosialansvarlig', b'Sosialansvarlig'), (b'Styremedlem', b'Styremedlem')])),
                ('about', models.TextField(verbose_name=b'about', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
