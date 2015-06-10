# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paddleusers', '0002_remove_paddleuser_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pic', models.ImageField(upload_to=b'images/', null=True, verbose_name=b'Profile picture', blank=True)),
                ('position', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'Board position', choices=[(b'Leder', b'Leder'), (b'Leder', b'Nestleder'), (b'\xc3\x98konomisjef', b'\xc3\x98konomisjef'), (b'Elvesjef', b'Elvesjef'), (b'Havsjef', b'Havsjef'), (b'Websjef', b'Websjef'), (b'Utstyrssjef hav', b'Utstyrssjef hav'), (b'Utstyressjef elv', b'Utstyressjef elv'), (b'Polosjef', b'Polosjef'), (b'Websjef', b'Websjef'), (b'Sosialansvarlig', b'Sosialansvarlig'), (b'Styremedlem', b'Styremedlem')])),
            ],
        ),
        migrations.RemoveField(
            model_name='paddleuser',
            name='user',
        ),
        migrations.DeleteModel(
            name='PaddleUser',
        ),
    ]
