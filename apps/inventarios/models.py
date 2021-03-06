from django.db import models
from apps.parametros.models import Sucursal
from django.core.exceptions import ValidationError


class Tipoproducto(models.Model):
    tpo_idtipos = models.CharField('Cód. Tipo/Producto', max_length=1, primary_key=True, default="P")
    tpo_detalle = models.CharField('Detalle', max_length=20)
    tpo_abrevia = models.CharField('Abreviatura', max_length=10)

    def __str__(self):
        return (self.tpo_detalle)


class Unidad(models.Model):

    und_idunida = models.CharField('Cód. Unidad', max_length=5, primary_key=True)
    und_detalle = models.CharField('Detalle', max_length=20)

    def __str__(self):
        return (self.und_detalle)


class Division(models.Model):

    div_detalle = models.CharField('Detalle', max_length=20)
    div_abrevia = models.CharField('Abreviatura', max_length=7)
    div_indicad = models.IntegerField('Un indicador', default=1)
    div_statreg = models.BooleanField('Status del Registro', default=True)

    def __str__(self):
        return (self.div_detalle)


class Tabtalla(models.Model):

    jgo_idtalla = models.CharField('Código de la Tabla', max_length=2)
    jgo_divisio = models.ForeignKey(Division)
    jgo_medid01 = models.CharField('Talla-01', max_length=6, null=True, blank=True)
    jgo_medid02 = models.CharField('Talla-02', max_length=6, null=True, blank=True)
    jgo_medid03 = models.CharField('Talla-03', max_length=6, null=True, blank=True)
    jgo_medid04 = models.CharField('Talla-04', max_length=6, null=True, blank=True)
    jgo_medid05 = models.CharField('Talla-05', max_length=6, null=True, blank=True)
    jgo_medid06 = models.CharField('Talla-06', max_length=6, null=True, blank=True)
    jgo_medid07 = models.CharField('Talla-07', max_length=6, null=True, blank=True)
    jgo_medid08 = models.CharField('Talla-08', max_length=6, null=True, blank=True)
    jgo_medid09 = models.CharField('Talla-09', max_length=6, null=True, blank=True)
    jgo_medid10 = models.CharField('Talla-10', max_length=6, null=True, blank=True)
    jgo_medid11 = models.CharField('Talla-11', max_length=6, null=True, blank=True)
    jgo_medid12 = models.CharField('Talla-12', max_length=6, null=True, blank=True)
    jgo_medid13 = models.CharField('Talla-13', max_length=6, null=True, blank=True)

    def get_shortcode(self):
        return "{}{}".format(self.jgo_divisio.pk, self.jgo_idtalla)

    def __str__(self):
        return self.get_shortcode()


class Marca(models.Model):

    mrk_idmarca = models.CharField('Código de  Marca', max_length=5, primary_key=True)
    mrk_detalle = models.CharField('Detalle', max_length=15)
    mrk_abrevia = models.CharField('Abreviatura', max_length=5)
    mrk_indicad = models.CharField('Indicador', max_length=1, default=1)
    mrk_statreg = models.BooleanField('Status del Registro', default=True)

    def __str__(self):
        return (self.mrk_detalle)


class Modelo(models.Model):

    mod_idmodel = models.CharField('Código de Modelo', max_length=5, primary_key=True)
    mod_idmarca = models.ForeignKey(Marca)
    mod_detalle = models.CharField('Detalle', max_length=20)
    mod_abrevia = models.CharField('Abreviatura', max_length=8)
    mod_tabtall = models.ForeignKey(Tabtalla, null=True, blank=True)
    mod_statreg = models.BooleanField('Status del Registro', default=True)

    def __str__(self):
        return (self.mod_detalle)


class Color(models.Model):

    col_idcolor = models.CharField('Código de Color', max_length=5, primary_key=True)
    col_detalle = models.CharField('Detalle', max_length=15)
    col_abrevia = models.CharField('Abreviatura', max_length=10)
    col_indicad = models.CharField('Indicador', max_length=1, default=1)
    col_statreg = models.BooleanField('Status del Registro', default=True)

    def __str__(self):
        return (self.col_detalle)


class Existencia(models.Model):
    exs_sucursa = models.ForeignKey(Sucursal)
    exs_iddivis = models.ForeignKey(Division)
    exs_idmarca = models.ForeignKey(Marca)
    exs_idmodel = models.ForeignKey(Modelo)
    exs_idcolor = models.ForeignKey(Color)
    exs_product = models.CharField('Cód. Producto', max_length=13, editable=False, unique=True, db_index=True)
    exs_detalle = models.CharField('Detalle del Producto', editable=False, max_length=45)
    exs_abrevia = models.CharField('Abreviatura del Producto', editable=False, max_length=30)
    exs_tpoprod = models.ForeignKey(Tipoproducto)
    exs_tabtall = models.CharField('Tabla de Tallas', editable=False, max_length=5, blank=True, null=True)
    exs_idunida = models.ForeignKey(Unidad)
    exs_saldinc = models.DecimalField('Saldo inicial', max_digits=11, decimal_places=4, blank=True, null=True)
    exs_ingreso = models.DecimalField('Ingresos', max_digits=11, decimal_places=4, blank=True, null=True)
    exs_egresos = models.DecimalField('Egresos', max_digits=11, decimal_places=4, blank=True, null=True)
    exs_saldact = models.DecimalField('Saldo Actual', max_digits=11, decimal_places=4, blank=True, null=True)
    exs_comprom = models.DecimalField('S.Compromet.(Ped. de Client)', max_digits=11, decimal_places=4, blank=True, null=True)
    exs_xconfir = models.DecimalField('S. x confirm.(Ped.a Proveed)', max_digits=11, decimal_places=4, blank=True, null=True)
    exs_dsponib = models.DecimalField('Saldo disponible', max_digits=11, decimal_places=4, blank=True, null=True)
    exs_feching = models.DateTimeField('Fecha de ult. Ingreso', blank=True, null=True)  # TODO: Manejar NULL
    exs_fechegr = models.DateTimeField('Fecha Ult. Egreso', blank=True, null=True)  # TODO: Manejar NULL
    exs_fechinv = models.DateTimeField('Fecha de inventario', blank=True, null=True)  # TODO: Manejar NULL
    exs_costant = models.DecimalField('Costo promedio Anterior', max_digits=15, decimal_places=4, null=True, blank=True)
    exs_dispant = models.DecimalField('Disponible Anterior', max_digits=15, decimal_places=4, null=True, blank=True)
    exs_costact = models.DecimalField('Costo Actual', max_digits=15, decimal_places=4, null=True, blank=True)
    exs_cosprom = models.DecimalField('Costo promedio Actual', max_digits=15, decimal_places=4, null=True, blank=True)
    exs_distrib = models.DecimalField('Distribuidor', max_digits=15, decimal_places=4, null=True, blank=True)
    exs_mayoris = models.DecimalField('Mayorista', max_digits=15, decimal_places=4, null=True, blank=True)
    exs_detalls = models.DecimalField('Detallista', max_digits=15, decimal_places=4, null=True, blank=True)
    exs_publico = models.DecimalField('Publico', max_digits=15, decimal_places=4, null=True, blank=True)
    exs_special = models.DecimalField('Especial', max_digits=15, decimal_places=4, null=True, blank=True)
    exs_imgprod = models.ImageField(upload_to="productos", blank=True)
    exs_statreg = models.BooleanField('Status del Registro', default=True)

    def get_tabtalla(self):
        return self.exs_idmodel.mod_tabtall

    def __str__(self):
        return self.exs_product

    def generate_id(self):
        product_id = "{0:01d}{1:02d}{2:03d}{3:03d}{4:03d}".format(
            self.exs_sucursa.suc_codgsuc,  # 2
            self.exs_iddivis.pk,  # 2
            # TODO: Definir si ID debe ser INT
            int(self.exs_idmarca.pk),  # 3
            int(self.exs_idmodel.pk),  # 3
            int(self.exs_idcolor.pk)   # 3
        )
        self._id = product_id
        return product_id

    def clean(self):
        super(Existencia, self).clean()
        queryset = Existencia.objects.filter(exs_product=self.generate_id())
        if self.pk:
            queryset = queryset.exclude(pk=self.pk)
        if queryset.exists():
            raise ValidationError("Ya existe un producto similar.")

    def save(self, *args, **kwargs):
        if self.exs_sucursa and self.exs_iddivis and self.exs_idmarca and self.exs_idmodel and self.exs_idcolor:
            self.exs_product = getattr(self, '_id', self.generate_id())
            self.exs_detalle = "{} {} {} {}".format(
                str(self.exs_idmarca.mrk_detalle),  # 3
                str(self.exs_iddivis.div_abrevia),  # 2
                str(self.exs_idmodel.mod_detalle),  # 3
                str(self.exs_idcolor.col_detalle)   # 3
            )
            self.exs_abrevia = "{} {} {} {}".format(
                str(self.exs_idmarca.mrk_abrevia),  # 05
                str(self.exs_iddivis.div_abrevia),  # 07
                str(self.exs_idmodel.mod_abrevia),  # 08
                str(self.exs_idcolor.col_abrevia)   # 10
            )[:30]  # TODO: Analizar si aumentar el 'max_length' a 33 (+3 por los espacios)

            self.exs_tabtall = "{}".format(
                str(self.exs_idmodel.mod_tabtall)  # 2
            ) if self.exs_idmodel.mod_tabtall else 'X'
        # TODO: Definir si amerita modificar los parámetros
        # TODO: Definir el max_length de CharField o poner TextField
        super(Existencia, self).save()


class Saldoxtalla(models.Model):
    tex_product = models.OneToOneField(Existencia, verbose_name='Saldo x talla', primary_key=True)
    tex_inici01 = models.DecimalField('Cant. inici-01', max_digits=11, decimal_places=4, null=True)
    tex_inici02 = models.DecimalField('Cant. inici-02', max_digits=11, decimal_places=4, null=True)
    tex_inici03 = models.DecimalField('Cant. inici-03', max_digits=11, decimal_places=4, null=True)
    tex_inici04 = models.DecimalField('Cant. inici-04', max_digits=11, decimal_places=4, null=True)
    tex_inici05 = models.DecimalField('Cant. inici-05', max_digits=11, decimal_places=4, null=True)
    tex_inici06 = models.DecimalField('Cant. inici-06', max_digits=11, decimal_places=4, null=True)
    tex_inici07 = models.DecimalField('Cant. inici-07', max_digits=11, decimal_places=4, null=True)
    tex_inici08 = models.DecimalField('Cant. inici-08', max_digits=11, decimal_places=4, null=True)
    tex_inici09 = models.DecimalField('Cant. inici-09', max_digits=11, decimal_places=4, null=True)
    tex_inici10 = models.DecimalField('Cant. inici-10', max_digits=11, decimal_places=4, null=True)
    tex_inici11 = models.DecimalField('Cant. inici-11', max_digits=11, decimal_places=4, null=True)
    tex_inici12 = models.DecimalField('Cant. inici-12', max_digits=11, decimal_places=4, null=True)
    tex_inici13 = models.DecimalField('Cant. inici-13', max_digits=11, decimal_places=4, null=True)

    tex_ingre01 = models.DecimalField('Cant. ingre-01', max_digits=11, decimal_places=4, null=True)
    tex_ingre02 = models.DecimalField('Cant. ingre-02', max_digits=11, decimal_places=4, null=True)
    tex_ingre03 = models.DecimalField('Cant. ingre-03', max_digits=11, decimal_places=4, null=True)
    tex_ingre04 = models.DecimalField('Cant. ingre-04', max_digits=11, decimal_places=4, null=True)
    tex_ingre05 = models.DecimalField('Cant. ingre-05', max_digits=11, decimal_places=4, null=True)
    tex_ingre06 = models.DecimalField('Cant. ingre-06', max_digits=11, decimal_places=4, null=True)
    tex_ingre07 = models.DecimalField('Cant. ingre-07', max_digits=11, decimal_places=4, null=True)
    tex_ingre08 = models.DecimalField('Cant. ingre-08', max_digits=11, decimal_places=4, null=True)
    tex_ingre09 = models.DecimalField('Cant. ingre-09', max_digits=11, decimal_places=4, null=True)
    tex_ingre10 = models.DecimalField('Cant. ingre-10', max_digits=11, decimal_places=4, null=True)
    tex_ingre11 = models.DecimalField('Cant. ingre-11', max_digits=11, decimal_places=4, null=True)
    tex_ingre12 = models.DecimalField('Cant. ingre-12', max_digits=11, decimal_places=4, null=True)
    tex_ingre13 = models.DecimalField('Cant. ingre-13', max_digits=11, decimal_places=4, null=True)

    tex_egres01 = models.DecimalField('Cant. egres-01', max_digits=11, decimal_places=4, null=True)
    tex_egres02 = models.DecimalField('Cant. egres-02', max_digits=11, decimal_places=4, null=True)
    tex_egres03 = models.DecimalField('Cant. egres-03', max_digits=11, decimal_places=4, null=True)
    tex_egres04 = models.DecimalField('Cant. egres-04', max_digits=11, decimal_places=4, null=True)
    tex_egres05 = models.DecimalField('Cant. egres-05', max_digits=11, decimal_places=4, null=True)
    tex_egres06 = models.DecimalField('Cant. egres-06', max_digits=11, decimal_places=4, null=True)
    tex_egres07 = models.DecimalField('Cant. egres-07', max_digits=11, decimal_places=4, null=True)
    tex_egres08 = models.DecimalField('Cant. egres-08', max_digits=11, decimal_places=4, null=True)
    tex_egres09 = models.DecimalField('Cant. egres-09', max_digits=11, decimal_places=4, null=True)
    tex_egres10 = models.DecimalField('Cant. egres-10', max_digits=11, decimal_places=4, null=True)
    tex_egres11 = models.DecimalField('Cant. egres-11', max_digits=11, decimal_places=4, null=True)
    tex_egres12 = models.DecimalField('Cant. egres-12', max_digits=11, decimal_places=4, null=True)
    tex_egres13 = models.DecimalField('Cant. egres-13', max_digits=11, decimal_places=4, null=True)

    tex_actua01 = models.DecimalField('Cant. actua-01', max_digits=11, decimal_places=4, null=True)
    tex_actua02 = models.DecimalField('Cant. actua-02', max_digits=11, decimal_places=4, null=True)
    tex_actua03 = models.DecimalField('Cant. actua-03', max_digits=11, decimal_places=4, null=True)
    tex_actua04 = models.DecimalField('Cant. actua-04', max_digits=11, decimal_places=4, null=True)
    tex_actua05 = models.DecimalField('Cant. actua-05', max_digits=11, decimal_places=4, null=True)
    tex_actua06 = models.DecimalField('Cant. actua-06', max_digits=11, decimal_places=4, null=True)
    tex_actua07 = models.DecimalField('Cant. actua-07', max_digits=11, decimal_places=4, null=True)
    tex_actua08 = models.DecimalField('Cant. actua-08', max_digits=11, decimal_places=4, null=True)
    tex_actua09 = models.DecimalField('Cant. actua-09', max_digits=11, decimal_places=4, null=True)
    tex_actua10 = models.DecimalField('Cant. actua-10', max_digits=11, decimal_places=4, null=True)
    tex_actua11 = models.DecimalField('Cant. actua-11', max_digits=11, decimal_places=4, null=True)
    tex_actua12 = models.DecimalField('Cant. actua-12', max_digits=11, decimal_places=4, null=True)
    tex_actua13 = models.DecimalField('Cant. actua-13', max_digits=11, decimal_places=4, null=True)

    tex_compr01 = models.DecimalField('Cant. compr-01', max_digits=11, decimal_places=4, null=True)
    tex_compr02 = models.DecimalField('Cant. compr-02', max_digits=11, decimal_places=4, null=True)
    tex_compr03 = models.DecimalField('Cant. compr-03', max_digits=11, decimal_places=4, null=True)
    tex_compr04 = models.DecimalField('Cant. compr-04', max_digits=11, decimal_places=4, null=True)
    tex_compr05 = models.DecimalField('Cant. compr-05', max_digits=11, decimal_places=4, null=True)
    tex_compr06 = models.DecimalField('Cant. compr-06', max_digits=11, decimal_places=4, null=True)
    tex_compr07 = models.DecimalField('Cant. compr-07', max_digits=11, decimal_places=4, null=True)
    tex_compr08 = models.DecimalField('Cant. compr-08', max_digits=11, decimal_places=4, null=True)
    tex_compr09 = models.DecimalField('Cant. compr-09', max_digits=11, decimal_places=4, null=True)
    tex_compr10 = models.DecimalField('Cant. compr-10', max_digits=11, decimal_places=4, null=True)
    tex_compr11 = models.DecimalField('Cant. compr-11', max_digits=11, decimal_places=4, null=True)
    tex_compr12 = models.DecimalField('Cant. compr-12', max_digits=11, decimal_places=4, null=True)
    tex_compr13 = models.DecimalField('Cant. compr-13', max_digits=11, decimal_places=4, null=True)

    tex_xconf01 = models.DecimalField('Cant. xconf-01', max_digits=11, decimal_places=4, null=True)
    tex_xconf02 = models.DecimalField('Cant. xconf-02', max_digits=11, decimal_places=4, null=True)
    tex_xconf03 = models.DecimalField('Cant. xconf-03', max_digits=11, decimal_places=4, null=True)
    tex_xconf04 = models.DecimalField('Cant. xconf-04', max_digits=11, decimal_places=4, null=True)
    tex_xconf05 = models.DecimalField('Cant. xconf-05', max_digits=11, decimal_places=4, null=True)
    tex_xconf06 = models.DecimalField('Cant. xconf-06', max_digits=11, decimal_places=4, null=True)
    tex_xconf07 = models.DecimalField('Cant. xconf-07', max_digits=11, decimal_places=4, null=True)
    tex_xconf08 = models.DecimalField('Cant. xconf-08', max_digits=11, decimal_places=4, null=True)
    tex_xconf09 = models.DecimalField('Cant. xconf-09', max_digits=11, decimal_places=4, null=True)
    tex_xconf10 = models.DecimalField('Cant. xconf-10', max_digits=11, decimal_places=4, null=True)
    tex_xconf11 = models.DecimalField('Cant. xconf-11', max_digits=11, decimal_places=4, null=True)
    tex_xconf12 = models.DecimalField('Cant. xconf-12', max_digits=11, decimal_places=4, null=True)
    tex_xconf13 = models.DecimalField('Cant. xconf-13', max_digits=11, decimal_places=4, null=True)

    tex_dispo01 = models.DecimalField('Cant. dispo-01', max_digits=11, decimal_places=4, null=True)
    tex_dispo02 = models.DecimalField('Cant. dispo-02', max_digits=11, decimal_places=4, null=True)
    tex_dispo03 = models.DecimalField('Cant. dispo-03', max_digits=11, decimal_places=4, null=True)
    tex_dispo04 = models.DecimalField('Cant. dispo-04', max_digits=11, decimal_places=4, null=True)
    tex_dispo05 = models.DecimalField('Cant. dispo-05', max_digits=11, decimal_places=4, null=True)
    tex_dispo06 = models.DecimalField('Cant. dispo-06', max_digits=11, decimal_places=4, null=True)
    tex_dispo07 = models.DecimalField('Cant. dispo-07', max_digits=11, decimal_places=4, null=True)
    tex_dispo08 = models.DecimalField('Cant. dispo-08', max_digits=11, decimal_places=4, null=True)
    tex_dispo09 = models.DecimalField('Cant. dispo-09', max_digits=11, decimal_places=4, null=True)
    tex_dispo10 = models.DecimalField('Cant. dispo-10', max_digits=11, decimal_places=4, null=True)
    tex_dispo11 = models.DecimalField('Cant. dispo-11', max_digits=11, decimal_places=4, null=True)
    tex_dispo12 = models.DecimalField('Cant. dispo-12', max_digits=11, decimal_places=4, null=True)
    tex_dispo13 = models.DecimalField('Cant. dispo-13', max_digits=11, decimal_places=4, null=True)

    def __str__(self):
        return str(self.tex_product)

    def save(self, *args, **kwargs):
        for index, saldotalla in enumerate(self.calc_saldact_tall(), start=1):
            setattr(self, "tex_actua{0:02d}".format(index), saldotalla)

        for index, saldotalla in enumerate(self.calc_saldisp_tall(), start=1):
            setattr(self, "tex_dispo{0:02d}".format(index), saldotalla)

        super(Saldoxtalla, self).save()

        self.tex_product.exs_saldinc = (
            (self.tex_inici01 or 0) +
            (self.tex_inici02 or 0) +
            (self.tex_inici03 or 0) +
            (self.tex_inici04 or 0) +
            (self.tex_inici05 or 0) +
            (self.tex_inici06 or 0) +
            (self.tex_inici07 or 0) +
            (self.tex_inici08 or 0) +
            (self.tex_inici09 or 0) +
            (self.tex_inici10 or 0) +
            (self.tex_inici11 or 0) +
            (self.tex_inici12 or 0) +
            (self.tex_inici13 or 0)
        )
        self.tex_product.exs_ingreso = (
            (self.tex_ingre01 or 0) +
            (self.tex_ingre02 or 0) +
            (self.tex_ingre03 or 0) +
            (self.tex_ingre04 or 0) +
            (self.tex_ingre05 or 0) +
            (self.tex_ingre06 or 0) +
            (self.tex_ingre07 or 0) +
            (self.tex_ingre08 or 0) +
            (self.tex_ingre09 or 0) +
            (self.tex_ingre10 or 0) +
            (self.tex_ingre11 or 0) +
            (self.tex_ingre12 or 0) +
            (self.tex_ingre13 or 0)
        )
        self.tex_product.exs_egresos = (
            (self.tex_egres01 or 0) +
            (self.tex_egres02 or 0) +
            (self.tex_egres03 or 0) +
            (self.tex_egres04 or 0) +
            (self.tex_egres05 or 0) +
            (self.tex_egres06 or 0) +
            (self.tex_egres07 or 0) +
            (self.tex_egres08 or 0) +
            (self.tex_egres09 or 0) +
            (self.tex_egres10 or 0) +
            (self.tex_egres11 or 0) +
            (self.tex_egres12 or 0) +
            (self.tex_egres13 or 0)
        )
        self.tex_product.exs_comprom = (
            (self.tex_compr01 or 0) +
            (self.tex_compr02 or 0) +
            (self.tex_compr03 or 0) +
            (self.tex_compr04 or 0) +
            (self.tex_compr05 or 0) +
            (self.tex_compr06 or 0) +
            (self.tex_compr07 or 0) +
            (self.tex_compr08 or 0) +
            (self.tex_compr09 or 0) +
            (self.tex_compr10 or 0) +
            (self.tex_compr11 or 0) +
            (self.tex_compr12 or 0) +
            (self.tex_compr13 or 0)
        )
        self.tex_product.exs_xconfir = (
            (self.tex_xconf01 or 0) +
            (self.tex_xconf02 or 0) +
            (self.tex_xconf03 or 0) +
            (self.tex_xconf04 or 0) +
            (self.tex_xconf05 or 0) +
            (self.tex_xconf06 or 0) +
            (self.tex_xconf07 or 0) +
            (self.tex_xconf08 or 0) +
            (self.tex_xconf09 or 0) +
            (self.tex_xconf10 or 0) +
            (self.tex_xconf11 or 0) +
            (self.tex_xconf12 or 0) +
            (self.tex_xconf13 or 0)
        )
        self.tex_product.exs_saldact = (
            (self.tex_inici01 or 0) + (self.tex_ingre01 or 0) - (self.tex_egres01 or 0) +
            (self.tex_inici02 or 0) + (self.tex_ingre02 or 0) - (self.tex_egres02 or 0) +
            (self.tex_inici03 or 0) + (self.tex_ingre03 or 0) - (self.tex_egres03 or 0) +
            (self.tex_inici04 or 0) + (self.tex_ingre04 or 0) - (self.tex_egres04 or 0) +
            (self.tex_inici05 or 0) + (self.tex_ingre05 or 0) - (self.tex_egres05 or 0) +
            (self.tex_inici06 or 0) + (self.tex_ingre06 or 0) - (self.tex_egres06 or 0) +
            (self.tex_inici07 or 0) + (self.tex_ingre07 or 0) - (self.tex_egres07 or 0) +
            (self.tex_inici08 or 0) + (self.tex_ingre08 or 0) - (self.tex_egres08 or 0) +
            (self.tex_inici09 or 0) + (self.tex_ingre09 or 0) - (self.tex_egres09 or 0) +
            (self.tex_inici10 or 0) + (self.tex_ingre10 or 0) - (self.tex_egres10 or 0) +
            (self.tex_inici11 or 0) + (self.tex_ingre11 or 0) - (self.tex_egres11 or 0) +
            (self.tex_inici12 or 0) + (self.tex_ingre12 or 0) - (self.tex_egres12 or 0) +
            (self.tex_inici13 or 0) + (self.tex_ingre13 or 0) - (self.tex_egres13 or 0)
        )
        self.tex_product.exs_dsponib = (
            (self.tex_inici01 or 0) + (self.tex_ingre01 or 0) - (self.tex_egres01 or 0) - (self.tex_compr01 or 0) +
            (self.tex_inici02 or 0) + (self.tex_ingre02 or 0) - (self.tex_egres02 or 0) - (self.tex_compr02 or 0) +
            (self.tex_inici03 or 0) + (self.tex_ingre03 or 0) - (self.tex_egres03 or 0) - (self.tex_compr03 or 0) +
            (self.tex_inici04 or 0) + (self.tex_ingre04 or 0) - (self.tex_egres04 or 0) - (self.tex_compr04 or 0) +
            (self.tex_inici05 or 0) + (self.tex_ingre05 or 0) - (self.tex_egres05 or 0) - (self.tex_compr05 or 0) +
            (self.tex_inici06 or 0) + (self.tex_ingre06 or 0) - (self.tex_egres06 or 0) - (self.tex_compr06 or 0) +
            (self.tex_inici07 or 0) + (self.tex_ingre07 or 0) - (self.tex_egres07 or 0) - (self.tex_compr07 or 0) +
            (self.tex_inici08 or 0) + (self.tex_ingre08 or 0) - (self.tex_egres08 or 0) - (self.tex_compr08 or 0) +
            (self.tex_inici09 or 0) + (self.tex_ingre09 or 0) - (self.tex_egres09 or 0) - (self.tex_compr09 or 0) +
            (self.tex_inici10 or 0) + (self.tex_ingre10 or 0) - (self.tex_egres10 or 0) - (self.tex_compr10 or 0) +
            (self.tex_inici11 or 0) + (self.tex_ingre11 or 0) - (self.tex_egres11 or 0) - (self.tex_compr11 or 0) +
            (self.tex_inici12 or 0) + (self.tex_ingre12 or 0) - (self.tex_egres12 or 0) - (self.tex_compr12 or 0) +
            (self.tex_inici13 or 0) + (self.tex_ingre13 or 0) - (self.tex_egres13 or 0) - (self.tex_compr13 or 0)
        )

        self.tex_product.save()

    def calc_saldact_tall(self):
        for talla in range(1, 14):
            yield (
                (getattr(self, "tex_inici{0:02d}".format(talla)) or 0) +
                (getattr(self, "tex_ingre{0:02d}".format(talla)) or 0) -
                (getattr(self, "tex_egres{0:02d}".format(talla)) or 0)
            )

    def calc_saldisp_tall(self):
        for index, talla in enumerate(self.calc_saldact_tall(), start=1):
            yield (
                talla -
                (getattr(self, "tex_compr{0:02d}".format(index)) or 0)
            )
