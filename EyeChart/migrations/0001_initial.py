# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-21 01:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=264)),
                ('patient_age', models.DecimalField(decimal_places=0, max_digits=3)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'other')], max_length=6)),
                ('left_eye_score', models.CharField(max_length=150)),
                ('right_eye_score', models.CharField(max_length=150)),
                ('both_eye_score', models.CharField(max_length=150)),
                ('notes', models.TextField()),
            ],
        ),
    ]
