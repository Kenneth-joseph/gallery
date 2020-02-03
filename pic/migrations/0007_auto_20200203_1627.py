# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-03 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pic', '0006_auto_20200203_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[(b'FS', b'Fashion'), (b'MS', b'Music'), (b'NT', b'Nature'), (b'AT', b'Art')], default=b'FS', max_length=2),
        ),
    ]
