# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='image',
            field=models.ImageField(blank=True, help_text='150x150px', upload_to='images/tours', verbose_name='Изображение тура'),
        ),
    ]
