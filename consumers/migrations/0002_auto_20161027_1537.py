# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 08:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('consumers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='start_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='buying',
            name='buy_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
