# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20170214_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='ISBN',
            field=models.CharField(default=1, max_length=13),
            preserve_default=False,
        ),
    ]
