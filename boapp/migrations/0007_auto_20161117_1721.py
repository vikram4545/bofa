# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-17 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boapp', '0006_holder_li'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='holder',
            name='li',
        ),
        migrations.AddField(
            model_name='number',
            name='li',
            field=models.CharField(default=' ', max_length=3000),
            preserve_default=False,
        ),
    ]
