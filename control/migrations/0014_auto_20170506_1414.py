# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-06 06:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0013_auto_20170506_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='author',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
