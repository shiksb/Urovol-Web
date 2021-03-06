# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-23 22:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DecimalField(decimal_places=1, max_digits=12)),
                ('raw_vol', models.DecimalField(decimal_places=1, max_digits=10)),
                ('las_vol', models.DecimalField(decimal_places=1, max_digits=10)),
                ('new_vol', models.DecimalField(decimal_places=1, max_digits=10)),
                ('cum_vol', models.DecimalField(decimal_places=1, max_digits=10)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='data',
            name='pi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.Pi'),
        ),
    ]
