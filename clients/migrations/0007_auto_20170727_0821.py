# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-27 08:21
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0006_auto_20170725_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientservice',
            name='quantity',
            field=models.PositiveIntegerField(db_index=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='clientservice',
            name='start_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='start date'),
        ),
    ]
