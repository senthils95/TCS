# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-18 07:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20170716_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracker',
            name='doi',
        ),
        migrations.RemoveField(
            model_name='tracker',
            name='dot',
        ),
    ]