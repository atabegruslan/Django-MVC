# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20160811233531 on 2016-08-15 05:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('rating', models.CharField(max_length=50)),
            ],
            options={
                'indexes': [],
            },
        ),
    ]
