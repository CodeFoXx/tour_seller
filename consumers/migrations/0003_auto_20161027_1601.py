# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 09:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumers', '0002_auto_20161027_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='buying',
            name='buy_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
