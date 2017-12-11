# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-18 22:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Controlador',
            fields=[
                ('ctl_idcontr', models.CharField(max_length=3, primary_key=True, serialize=False, verbose_name='Cód. del control de secuencia')),
                ('ctl_detalle', models.CharField(max_length=20, verbose_name='Detalle que documento  controla')),
                ('ctl_abrevia', models.CharField(max_length=10, verbose_name='Abreviatura')),
                ('ctl_secuenc', models.IntegerField(verbose_name='Secuencia del documento')),
            ],
        ),
    ]