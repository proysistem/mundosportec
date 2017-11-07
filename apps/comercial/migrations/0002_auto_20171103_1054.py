# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-03 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comercial', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movinvent',
            name='mvi_talla14',
        ),
        migrations.RemoveField(
            model_name='movinvent',
            name='mvi_talla15',
        ),
        migrations.AddField(
            model_name='movinvent',
            name='mvi_factura',
            field=models.IntegerField(blank=True, null=True, verbose_name='Núm. de factrura'),
        ),
        migrations.AddField(
            model_name='movinvent',
            name='mvi_pedidos',
            field=models.IntegerField(blank=True, null=True, verbose_name='Núm. de pedido'),
        ),
    ]
