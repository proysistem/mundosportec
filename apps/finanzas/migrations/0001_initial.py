# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 15:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parametros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cja_cotizac', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Cotización')),
                ('cja_fchultm', models.DateField(verbose_name='Fecha de último movimiento')),
                ('cja_inicash', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Saldo Inic.Cash')),
                ('cja_ingcash', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Ingresos Cash')),
                ('cja_egrcash', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Egresos Cash')),
                ('cja_salcash', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Saldo Actual Cash')),
                ('cja_inicchq', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Saldo Inic.Cheq.')),
                ('cja_ingrchq', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Ingresos Cheq.')),
                ('cja_egrechq', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Egresos Cheq.')),
                ('cja_saldchq', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Saldo Actual Cheq.')),
                ('cja_inictjc', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Saldo Inic.T/CR.')),
                ('cja_ingrtjc', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Ingresos T/CR.')),
                ('cja_egretjc', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Egresos T/CR.')),
                ('cja_saldtjc', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Saldo Actual T/CR.')),
                ('cja_inicred', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Saldo Inic.Cred.')),
                ('cja_ingcred', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Ingresos Cred.')),
                ('cja_egrcred', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Egresos Cred.')),
                ('cja_salcred', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Saldo Actual Cred.')),
                ('cja_inicotr', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Saldo Inic.Otro')),
                ('cja_ingrotr', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Ingresos Otro')),
                ('cja_egreotr', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Egresos Otro')),
                ('cja_saldotr', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Saldo Actual Otro')),
                ('cja_fcharqe', models.DateField(verbose_name='Fecha de Arqueo/Caja')),
                ('cja_numarqe', models.IntegerField(verbose_name='Núm. De Arqueo')),
                ('cja_arqefec', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Arq. Cash')),
                ('cja_arqcheq', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Arq. Cheq.')),
                ('cja_arqtjcr', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Arq. T/CR.')),
                ('cja_arqcred', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Arq. Crédito')),
                ('cja_arqotro', models.DecimalField(decimal_places=4, max_digits=15, verbose_name='Arq.Otros')),
            ],
        ),
        migrations.CreateModel(
            name='Cajera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cjr_frsname', models.CharField(max_length=15, verbose_name='Primer Nombre')),
                ('cjr_midname', models.CharField(max_length=15, verbose_name='Segundo Nombre')),
                ('cjr_secmane', models.CharField(max_length=25, verbose_name='Apellidos')),
                ('cjr_fechnac', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('cjr_direcci', models.CharField(max_length=50, verbose_name='Direccion Domiciliaria')),
                ('cjr_telefon', models.CharField(max_length=15, verbose_name='Telefono')),
                ('cjr_celular', models.CharField(max_length=15, verbose_name='Celular')),
                ('cjr_correoe', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('cjr_imgcjer', models.ImageField(upload_to='cajeras')),
                ('cjr_rgunico', models.IntegerField(verbose_name='Registro Unico')),
                ('cjr_categor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parametros.Categoria')),
                ('cjr_ciudade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parametros.Ciudad')),
                ('cjr_country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parametros.Pais')),
                ('cjr_estados', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parametros.Provincia')),
                ('cjr_zipcodg', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parametros.Zipcodigo')),
            ],
        ),
        migrations.CreateModel(
            name='Moneda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mda_detalle', models.CharField(max_length=25, verbose_name='Detalle')),
                ('mda_abrevia', models.CharField(max_length=7, verbose_name='Abreviatura')),
                ('mda_cotizac', models.DecimalField(decimal_places=4, max_digits=11, verbose_name='Cotización ')),
                ('mda_mndofic', models.CharField(max_length=25, verbose_name='Moneda Oficial')),
                ('mda_abrofic', models.CharField(max_length=15, verbose_name='Abrev. Moneda oficial')),
            ],
        ),
        migrations.CreateModel(
            name='Movicaja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mcj_fechmov', models.DateField(verbose_name='Fecha')),
                ('mcj_cotizac', models.DecimalField(decimal_places=4, max_digits=11, verbose_name='Cotización')),
                ('mcj_numdocu', models.IntegerField(verbose_name='Documento origen')),
                ('mcj_valcash', models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Cash')),
                ('mcj_valcheq', models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Cheque')),
                ('mcj_valtjcr', models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='T./Crédito')),
                ('mcj_valcred', models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Crédito personal')),
                ('mcj_valotro', models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Internet (Paypal)')),
                ('mcj_cajanum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finanzas.Caja')),
                ('mcj_cajeras', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finanzas.Cajera')),
                ('mcj_monedas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finanzas.Moneda')),
                ('mcj_motivos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametros.Motivo')),
                ('mcj_sucursa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametros.Sucursal')),
                ('mcj_tipomov', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametros.Tipomovim')),
            ],
        ),
        migrations.AddField(
            model_name='caja',
            name='cja_cajeras',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='finanzas.Cajera'),
        ),
        migrations.AddField(
            model_name='caja',
            name='cja_monedas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='finanzas.Moneda'),
        ),
    ]