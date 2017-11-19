# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-14 04:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comercial', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='id',
        ),
        migrations.RemoveField(
            model_name='movinvent',
            name='id',
        ),
        migrations.AlterField(
            model_name='factura',
            name='fac_fechfac',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='fecha de la factura'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='fac_idfactu',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Núm. de Factura'),
        ),
        migrations.AlterField(
            model_name='movinvent',
            name='mvi_factura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comercial.Factura', verbose_name='Núm. de factura'),
        ),
        migrations.AlterField(
            model_name='movinvent',
            name='mvi_nummovi',
            field=models.AutoField(default=1, primary_key=True, serialize=False, verbose_name='Núm. de movimiento'),
            preserve_default=False,
        ),
    ]