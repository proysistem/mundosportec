# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-15 19:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comercial', '0002_auto_20171113_2308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='fac_mvinven',
        ),
        migrations.AlterField(
            model_name='factura',
            name='fac_fechfac',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de la factura'),
        ),
    ]
