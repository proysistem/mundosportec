# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-15 01:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parametros', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='controlador',
            name='ctl_abrevia',
        ),
        migrations.RemoveField(
            model_name='controlador',
            name='ctl_detalle',
        ),
        migrations.RemoveField(
            model_name='controlador',
            name='ctl_secuenc',
        ),
        migrations.AddField(
            model_name='controlador',
            name='ctl_secue01',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Secuencia 01'),
        ),
        migrations.AddField(
            model_name='controlador',
            name='ctl_secue02',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Secuencia 02'),
        ),
        migrations.AddField(
            model_name='controlador',
            name='ctl_secue03',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Secuencia 03'),
        ),
        migrations.AddField(
            model_name='controlador',
            name='ctl_secue04',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Secuencia 04'),
        ),
        migrations.AddField(
            model_name='controlador',
            name='ctl_secue05',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Secuencia 05'),
        ),
        migrations.AddField(
            model_name='controlador',
            name='ctl_secue06',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Secuencia 06'),
        ),
        migrations.AddField(
            model_name='controlador',
            name='ctl_secue07',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Secuencia 07'),
        ),
        migrations.AddField(
            model_name='controlador',
            name='ctl_secue08',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Secuencia 08'),
        ),
        migrations.AddField(
            model_name='controlador',
            name='ctl_secue09',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Secuencia 09'),
        ),
        migrations.AddField(
            model_name='controlador',
            name='ctl_secue10',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Secuencia 10'),
        ),
        migrations.RemoveField(
            model_name='controlador',
            name='ctl_idcontr',
        ),
        migrations.AddField(
            model_name='controlador',
            name='ctl_idcontr',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Cód. del control de secuencia'),
        ),
        migrations.AddField(
            model_name='controlador',
            name='ctl_sucrsal',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='parametros.Sucursal'),
            preserve_default=False,
        ),
    ]
