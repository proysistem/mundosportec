# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-17 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comercial', '0009_compra'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingreso',
            name='ing_facprov',
            field=models.CharField(default='', max_length=15, verbose_name='Nº Fac. Proveedor'),
            preserve_default=False,
        ),
    ]
