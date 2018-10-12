# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-12 20:39
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osf', '0129_merge_20180910_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='issue_choices',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=31), blank=True, default=list, size=None),
        ),
        migrations.AddField(
            model_name='collection',
            name='program_area_choices',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=31), blank=True, default=list, size=None),
        ),
        migrations.AddField(
            model_name='collection',
            name='volume_choices',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=31), blank=True, default=list, size=None),
        ),
        migrations.AddField(
            model_name='collectionsubmission',
            name='issue',
            field=models.CharField(blank=True, max_length=31),
        ),
        migrations.AddField(
            model_name='collectionsubmission',
            name='program_area',
            field=models.CharField(blank=True, max_length=31),
        ),
        migrations.AddField(
            model_name='collectionsubmission',
            name='volume',
            field=models.CharField(blank=True, max_length=31),
        ),
    ]