# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-19 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20161119_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='answer',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
