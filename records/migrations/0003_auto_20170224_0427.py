# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-24 04:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_auto_20170122_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='cum_vol',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='data',
            name='las_vol',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='data',
            name='new_vol',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='data',
            name='raw_vol',
            field=models.CharField(max_length=10),
        ),
    ]
