from django.db import models
# from django.core.exceptions import ValidationError


class TimeStampModel(models.Model):
    fch_creacion = models.DateTimeField(auto_now_add=True)
    fch_modifica = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Pais(models.Model):
    pai_detalle = models.CharField("Nombre", max_length=25)
    pai_abrevia = models.CharField("Abreviatura", max_length=10)

    def __str__(self):
        return self.pai_detalle


class Provincia(models.Model):
    est_country = models.ForeignKey(Pais)
    est_detalle = models.CharField("Nombre", max_length=25)
    est_abrevia = models.CharField("Abreviatura", max_length=10)
    est_capital = models.CharField("Capital", max_length=30)

    def __str__(self):
        return "%s" % (self.est_detalle)


class Ciudad(models.Model):
    ciu_estados = models.ForeignKey(Provincia)
    ciu_country = models.ForeignKey(Pais)
    ciu_nombres = models.CharField("Nombre", max_length=25)
    ciu_abrevia = models.CharField("Abreviatura", max_length=10)

    def __str__(self):
        return "%s" % (self.ciu_nombres)
        # return "%s %s %s" % (self.ciu_estados, self.ciu_country, self.ciu_nombres)


class Zipcodigo(models.Model):
    zip_idzipco = models.CharField("Código Postal", max_length=15)
    zip_idciuda = models.ForeignKey(Ciudad)
    zip_estados = models.ForeignKey(Provincia)
    zip_country = models.ForeignKey(Pais)

    def __str__(self):
        return "%s" % (self.zip_idzipco)


class Sucursal(models.Model):
    suc_codgsuc = models.PositiveIntegerField("Cód.Sucursal", unique=True, db_index=True)
    suc_nombres = models.CharField("Nombre", max_length=30)
    suc_abrevia = models.CharField("Abreviatura", max_length=15)
    suc_direcci = models.CharField("Dirección", max_length=45)
    suc_ciudads = models.ForeignKey(Ciudad)
    suc_estados = models.ForeignKey(Provincia)
    suc_country = models.ForeignKey(Pais)
    suc_zipcodg = models.ForeignKey(Zipcodigo)
    suc_impuest = models.PositiveIntegerField("IVA/Impuesto %", default=12)
    suc_statreg = models.CharField("Status del Registro", max_length=1)

    def __str__(self):
        return "%s %s" % (self.suc_codgsuc, self.suc_nombres)


class Categoria(models.Model):
    ktg_detalle = models.CharField('Detalle', max_length=15)
    ktg_abrevia = models.CharField('Abreviatura', max_length=7)


# class Tipomovim(models.Model):

#     tmv_detalle = models.CharField('Detalle', max_length=15)
#     tmv_abrevia = models.CharField('Abreviatura', max_length=10)


# class Motivo(models.Model):

#     mot_detalle = models.CharField('Detalle', max_length=20)
#     mot_abrevia = models.CharField('Abreviatura', max_length=10)

class Controlador(models.Model):
    ctl_idcontr = models.AutoField('Cód. del control de secuencia', primary_key=True)
    ctl_sucrsal = models.OneToOneField('Sucursal')
    ctl_secue01 = models.PositiveIntegerField('Secuencia 01 (Factura)', null=True, blank=True)
    ctl_secue02 = models.PositiveIntegerField('Secuencia 02', null=True, blank=True)
    ctl_secue03 = models.PositiveIntegerField('Secuencia 03', null=True, blank=True)
    ctl_secue04 = models.PositiveIntegerField('Secuencia 04', null=True, blank=True)
    ctl_secue05 = models.PositiveIntegerField('Secuencia 05', null=True, blank=True)
    ctl_secue06 = models.PositiveIntegerField('Secuencia 06', null=True, blank=True)
    ctl_secue07 = models.PositiveIntegerField('Secuencia 07', null=True, blank=True)
    ctl_secue08 = models.PositiveIntegerField('Secuencia 08', null=True, blank=True)
    ctl_secue09 = models.PositiveIntegerField('Secuencia 09', null=True, blank=True)
    ctl_secue10 = models.PositiveIntegerField('Secuencia 10', null=True, blank=True)

    def __str__(self):
        return "%s" % (self.ctl_sucrsal if self.ctl_sucrsal else 'Controlador')
