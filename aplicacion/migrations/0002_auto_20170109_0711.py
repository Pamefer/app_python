# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-09 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codigo',
            name='idcodigo',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
