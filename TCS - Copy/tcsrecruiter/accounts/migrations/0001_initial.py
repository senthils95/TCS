
# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-31 10:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Requirement_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asn_date', models.DateTimeField(verbose_name=b'date assigned')),
                ('stat', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Requirements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rgs_id', models.CharField(max_length=20, unique=True)),
                ('role', models.CharField(max_length=20)),
                ('rskill', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='requirement_details',
            name='rgs_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Requirements'),
        ),
    ]