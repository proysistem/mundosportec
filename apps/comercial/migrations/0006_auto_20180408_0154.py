# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-08 06:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comercial', '0005_auto_20180404_1455'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingreso',
            old_name='ing_fechped',
            new_name='ing_feching',
        ),
    ]
