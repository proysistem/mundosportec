# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 03:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comercial', '0003_auto_20171107_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='movinvent',
            name='mvi_nummovi',
            field=models.IntegerField(blank=True, null=True, verbose_name='Núm. de movimiento'),
        ),
    ]
