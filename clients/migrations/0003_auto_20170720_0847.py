# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-20 07:47
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20170718_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='installation',
            field=models.CharField(choices=[('not_installed', 'not installed'), ('process', 'process'), ('installed', 'installed')], db_index=True, default='not_installed', max_length=20),
        ),
        migrations.AlterField(
            model_name='client',
            name='login',
            field=models.CharField(db_index=True, max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(4), django.core.validators.RegexValidator(code='invalid_login', message='Enter a valid login. This value may contain only lowercase letters, numbers, and "-" character.', regex='^[a-z0-9\\-]*$')]),
        ),
    ]