# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-19 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aste', '0003_auto_20180619_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asta',
            name='foto',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
