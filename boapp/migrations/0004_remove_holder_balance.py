# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-16 20:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boapp', '0003_number_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='holder',
            name='balance',
        ),
    ]
