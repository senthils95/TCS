# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-01 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20170601_0832'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('rgs_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=200)),
                ('rskill', models.TextField()),
                ('texp', models.DecimalField(decimal_places=2, max_digits=4)),
                ('branch', models.CharField(max_length=200)),
                ('iou', models.CharField(max_length=200)),
                ('riou', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('asn_date', models.DateTimeField(verbose_name=b'date assigned')),
                ('rbranch', models.CharField(max_length=200)),
                ('sbranch', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
