# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 09:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_remove_tour_booking'),
        ('consumers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='tour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tours.Tour'),
        ),
    ]
