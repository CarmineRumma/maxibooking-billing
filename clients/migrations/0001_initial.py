# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-18 11:14
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('login', models.CharField(db_index=True, max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(6)])),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True, verbose_name='e-mail')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(db_index=True, max_length=50)),
                ('name', models.CharField(db_index=True, max_length=255, validators=[django.core.validators.MinLengthValidator(2)])),
                ('description', models.TextField(blank=True, db_index=True, null=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('status', models.CharField(choices=[('not_confirmed', 'not confirmed'), ('active', 'active'), ('disabled', 'disabled'), ('archived', 'archived')], db_index=True, default='not_confirmed', max_length=20)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clients_client_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clients_client_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]