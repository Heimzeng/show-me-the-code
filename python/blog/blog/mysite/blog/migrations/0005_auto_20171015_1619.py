# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 08:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20171015_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='time',
            new_name='date',
        ),
    ]
