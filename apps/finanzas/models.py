from django.db import models
from apps.parametros.models import Pais, Provincia, Ciudad, Zipcodigo, Sucursal, Motivo, Tipomovim, Categoria


class Moneda(models.Model):

    mda_detalle = models.CharField('Detalle', max_length=25)
    mda_abrevia = models.CharField('Abreviatura', max_length=7)
    mda_cotizac = models.DecimalField('Cotización ', max_digits=11, decimal_places=4)
    mda_mndofic = models.CharField('Moneda Oficial', max_length=25)
    mda_abrofic = models.CharField('Abrev. Moneda oficial', max_length=15)


class Cajera(models.Model):

    cjr_frsname = models.CharField('Primer Nombre', max_length=15)
    cjr_midname = models.CharField('Segundo Nombre', max_length=15)
    cjr_secmane = models.CharField('Apellidos', max_length=25)
    cjr_fechnac = models.DateField('Fecha de Nacimiento')
    cjr_direcci = models.CharField('Direccion Domiciliaria', max_length=50)
    cjr_ciudade = models.ForeignKey(Ciudad, null=True, blank=True)
    cjr_estados = models.ForeignKey(Provincia, null=True, blank=True)
    cjr_country = models.ForeignKey(Pais, null=True, blank=True)
    cjr_zipcodg = models.ForeignKey(Zipcodigo, null=True, blank=True)
    cjr_telefon = models.CharField('Telefono', max_length=15)
    cjr_celular = models.CharField('Celular', max_length=15)
    cjr_correoe = models.EmailField('e-mail')
    cjr_imgcjer = models.ImageField(upload_to="cajeras")
    cjr_rgunico = models.IntegerField('Registro Unico')
    cjr_categor = models.ForeignKey(Categoria, null=True, blank=True)


class Caja(models.Model):

    cja_monedas = models.ForeignKey(Moneda, null=True, blank=True)
    cja_cotizac = models.DecimalField('Cotización', max_digits=15, decimal_places=4)
    cja_fchultm = models.DateField('Fecha de último movimiento')
    cja_cajeras = models.ForeignKey(Cajera, null=True, blank=True)
    cja_inicash = models.DecimalField('Saldo Inic.Cash', max_digits=15, decimal_places=4)
    cja_ingcash = models.DecimalField('Ingresos Cash', max_digits=15, decimal_places=4)
    cja_egrcash = models.DecimalField('Egresos Cash', max_digits=15, decimal_places=4)
    cja_salcash = models.DecimalField('Saldo Actual Cash', max_digits=15, decimal_places=4)
    cja_inicchq = models.DecimalField('Saldo Inic.Cheq.', max_digits=15, decimal_places=4)
    cja_ingrchq = models.DecimalField('Ingresos Cheq.', max_digits=15, decimal_places=4)
    cja_egrechq = models.DecimalField('Egresos Cheq.', max_digits=15, decimal_places=4)
    cja_saldchq = models.DecimalField('Saldo Actual Cheq.', max_digits=15, decimal_places=4)
    cja_inictjc = models.DecimalField('Saldo Inic.T/CR.', max_digits=15, decimal_places=4)
    cja_ingrtjc = models.DecimalField('Ingresos T/CR.', max_digits=15, decimal_places=4)
    cja_egretjc = models.DecimalField('Egresos T/CR.', max_digits=15, decimal_places=4)
    cja_saldtjc = models.DecimalField('Saldo Actual T/CR.', max_digits=15, decimal_places=4)
    cja_inicred = models.DecimalField('Saldo Inic.Cred.', max_digits=15, decimal_places=4)
    cja_ingcred = models.DecimalField('Ingresos Cred.', max_digits=15, decimal_places=4)
    cja_egrcred = models.DecimalField('Egresos Cred.', max_digits=15, decimal_places=4)
    cja_salcred = models.DecimalField('Saldo Actual Cred.', max_digits=15, decimal_places=4)
    cja_inicotr = models.DecimalField('Saldo Inic.Otro', max_digits=15, decimal_places=4)
    cja_ingrotr = models.DecimalField('Ingresos Otro', max_digits=15, decimal_places=4)
    cja_egreotr = models.DecimalField('Egresos Otro', max_digits=15, decimal_places=4)
    cja_saldotr = models.DecimalField('Saldo Actual Otro', max_digits=15, decimal_places=4)
    cja_fcharqe = models.DateField('Fecha de Arqueo/Caja')
    cja_numarqe = models.IntegerField('Núm. De Arqueo')
    cja_arqefec = models.DecimalField('Arq. Cash', max_digits=15, decimal_places=4)
    cja_arqcheq = models.DecimalField('Arq. Cheq.', max_digits=15, decimal_places=4)
    cja_arqtjcr = models.DecimalField('Arq. T/CR.', max_digits=15, decimal_places=4)
    cja_arqcred = models.DecimalField('Arq. Crédito', max_digits=15, decimal_places=4)
    cja_arqotro = models.DecimalField('Arq.Otros', max_digits=15, decimal_places=4)


class Movicaja(models.Model):
    mcj_sucursa = models.ForeignKey(Sucursal)
    mcj_fechmov = models.DateField('Fecha')
    mcj_cajanum = models.ForeignKey(Caja)
    mcj_cajeras = models.ForeignKey(Cajera)
    mcj_monedas = models.ForeignKey(Moneda)
    mcj_cotizac = models.DecimalField('Cotización', max_digits=11, decimal_places=4)
    mcj_tipomov = models.ForeignKey(Tipomovim)
    mcj_motivos = models.ForeignKey(Motivo)
    mcj_numdocu = models.IntegerField('Documento origen')
    mcj_valcash = models.DecimalField('Cash', max_digits=15, decimal_places=4, null=True, blank=True)
    mcj_valcheq = models.DecimalField('Cheque', max_digits=15, decimal_places=4, null=True, blank=True)
    mcj_valtjcr = models.DecimalField('T./Crédito', max_digits=15, decimal_places=4, null=True, blank=True)
    mcj_valcred = models.DecimalField('Crédito personal', max_digits=15, decimal_places=4, null=True, blank=True)
    mcj_valotro = models.DecimalField('Internet (Paypal)', max_digits=15, decimal_places=4, null=True, blank=True)
