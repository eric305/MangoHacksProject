# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-02-03 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180203_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about_me',
            field=models.CharField(default=None, max_length=500),
            preserve_default=False,
        ),
    ]
