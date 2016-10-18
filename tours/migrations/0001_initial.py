# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-18 16:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('places', '0001_initial'),
        ('airlines', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField()),
                ('start_date', models.DateTimeField()),
                ('fin_date', models.DateTimeField()),
                ('capacity', models.PositiveIntegerField()),
                ('image', models.ImageField(blank=True, help_text='150x150px', upload_to='images/tours/', verbose_name='Изображение тура')),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airlines.Airline')),
                ('departure_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.City')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.Hotel')),
                ('tour_operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
