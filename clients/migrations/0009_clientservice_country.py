# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-02 10:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0008_auto_20170731_0922'),
        ('clients', '0008_auto_20170728_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientservice',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='hotels.Country', verbose_name='country'),
            preserve_default=False,
        ),
    ]
