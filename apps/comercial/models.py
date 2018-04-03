from django.db import models
from apps.finanzas.models import Cajera, Caja, Moneda
from apps.inventarios.models import Existencia, Unidad
from apps.parametros.models import Pais, Provincia, Ciudad, Zipcodigo, Sucursal, Categoria, Controlador
from apps.parametros.choices import TIPO_MOV_CHOICES
from django.utils import timezone

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction


class Cliente(models.Model):
    clt_frsname = models.CharField('Primer Nombre', max_length=15)
    clt_midname = models.CharField('Segundo Nombre', max_length=15)
    clt_secmane = models.CharField('Apellidos', max_length=25)
    clt_fechnac = models.DateField('Fecha de Nacimiento')
    clt_direcci = models.CharField('Direccion Domiciliaria', max_length=50)
    clt_ciudade = models.ForeignKey(Ciudad, null=True, blank=True)
    clt_estados = models.ForeignKey(Provincia, null=True, blank=True)
    cli_country = models.ForeignKey(Pais, null=True, blank=True)
    clt_zipcodg = models.ForeignKey(Zipcodigo, null=True, blank=True)
    clt_telefon = models.CharField('Telefono', max_length=15, blank=True)
    clt_celular = models.CharField('Celular', max_length=15, blank=True)
    clt_correoe = models.EmailField('e-mail')
    clt_imgclte = models.ImageField(upload_to="clientes", blank=True)
    clt_rgunico = models.CharField('Registro Unico', max_length=20, blank=True)
    clt_categor = models.ForeignKey(Categoria, null=True, blank=True)

    def __str__(self):
        return self.clt_frsname


class Proveedor(models.Model):

    prv_frsname = models.CharField('Primer Nombre', max_length=15)
    prv_midname = models.CharField('Segundo Nombre', max_length=15)
    prv_secmane = models.CharField('Apellidos', max_length=25)
    prv_fechnac = models.DateField('Fecha de Nacimiento', )
    prv_direcci = models.CharField('Direccion Domiciliaria', max_length=45)
    prv_ciudade = models.ForeignKey(Ciudad, null=True, blank=True)
    prv_estados = models.ForeignKey(Provincia, null=True, blank=True)
    prv_country = models.ForeignKey(Pais, null=True, blank=True)
    prv_zipcodg = models.ForeignKey(Zipcodigo, null=True, blank=True)
    prv_telefon = models.CharField('Telefono', max_length=15)
    prv_celular = models.CharField('Celular', max_length=15)
    prv_correoe = models.EmailField('e-mail')
    prv_imgprov = models.ImageField(upload_to="proveedores", blank=True)
    prv_rgunico = models.CharField('Registro Unico', max_length=20, blank=True)
    prv_categor = models.ForeignKey(Categoria, null=True, blank=True)


class Vendedor(models.Model):

    vnd_frsname = models.CharField('Primer Nombre', max_length=15)
    vnd_midname = models.CharField('Segundo Nombre', max_length=15)
    vnd_secmane = models.CharField('Apellidos', max_length=25)
    vnd_fechnac = models.DateField('Fecha de Nacimiento', )
    vnd_direcci = models.CharField('Direccion Domiciliaria', max_length=45)
    vnd_ciudade = models.ForeignKey(Ciudad, null=True, blank=True)
    vnd_estados = models.ForeignKey(Provincia, null=True, blank=True)
    vnd_country = models.ForeignKey(Pais, null=True, blank=True)
    vnd_zipcodg = models.ForeignKey(Zipcodigo, null=True, blank=True)
    vnd_telefon = models.CharField('Telefono', max_length=15, blank=True)
    vnd_ncelula = models.CharField('Celular', max_length=15, blank=True)
    vnd_correoe = models.EmailField('e-mail')
    vnd_addrimg = models.ImageField(upload_to="vendedores", blank=True)
    vnd_rgunico = models.CharField('Registro Unico', max_length=20, blank=True)
    vnd_categor = models.ForeignKey(Categoria, null=True, blank=True)

    def __str__(self):
        return self.vnd_frsname


class Ingreso(models.Model):
    ing_ningres = models.AutoField('Núm. de Ingreso', primary_key=True)
    ing_tipomov = models.PositiveIntegerField("Tipo de movimiento", choices=TIPO_MOV_CHOICES, default=TIPO_MOV_CHOICES.INGRESO)
    ing_fechped = models.DateField('Fecha de compra')
    ing_proveed = models.ForeignKey(Proveedor)
    ing_vendedo = models.ForeignKey(Vendedor, null=True, blank=True)
    ing_statreg = models.CharField('Status del Registro', max_length=1, default=1)
    # 1=En proceso, 2=Facturada, 7=Anulada, 9=Eliminada
    ing_sucursa = models.ForeignKey(Sucursal, null=True, blank=True)

    def __str__(self):
        return str(self.ing_ningres)


class Pedido(models.Model):
    ped_npedido = models.AutoField('Núm. de Pedido', primary_key=True)
    ped_tipomov = models.PositiveIntegerField("Tipo de movimiento", choices=TIPO_MOV_CHOICES, default=TIPO_MOV_CHOICES.EGRESO)
    ped_fechped = models.DateField('Fecha de pedido')
    ped_cliente = models.ForeignKey(Cliente)
    ped_vendedo = models.ForeignKey(Vendedor, null=True, blank=True)
    ped_statreg = models.CharField('Status del Registro', max_length=1, default=1)
    # 1=En proceso, 2=Facturada, 7=Anulada, 9=Eliminada
    ped_sucursa = models.ForeignKey(Sucursal, null=True, blank=True)

    def __str__(self):
        return str(self.ped_npedido)


class Movinvent(models.Model):
    mvi_nummovi = models.AutoField('Núm. de movimiento', primary_key=True)
    mvi_npedido = models.ForeignKey('Pedido', verbose_name='Núm. de pedido', null=True, blank=True)

    mvi_fechmov = models.DateField('Fecha')
    mvi_tipomov = models.PositiveIntegerField("Tipo de movimiento", choices=TIPO_MOV_CHOICES)
    mvi_vendedo = models.ForeignKey(Vendedor)
    mvi_cliente = models.ForeignKey(Cliente)
    mvi_product = models.ForeignKey(Existencia)
    mvi_unidade = models.CharField("Unidad", max_length=5)

    mvi_talla01 = models.DecimalField('Talla 01', max_digits=11, decimal_places=2, null=True, blank=True)
    mvi_talla02 = models.DecimalField('Talla 02', max_digits=11, decimal_places=2, null=True, blank=True)
    mvi_talla03 = models.DecimalField('Talla 03', max_digits=11, decimal_places=2, null=True, blank=True)
    mvi_talla04 = models.DecimalField('Talla 04', max_digits=11, decimal_places=2, null=True, blank=True)
    mvi_talla05 = models.DecimalField('Talla 05', max_digits=11, decimal_places=2, null=True, blank=True)
    mvi_talla06 = models.DecimalField('Talla 06', max_digits=11, decimal_places=2, null=True, blank=True)
    mvi_talla07 = models.DecimalField('Talla 07', max_digits=11, decimal_places=2, null=True, blank=True)
    mvi_talla08 = models.DecimalField('Talla 08', max_digits=11, decimal_places=2, null=True, blank=True)
    mvi_talla09 = models.DecimalField('Talla 09', max_digits=11, decimal_places=2, null=True, blank=True)
    mvi_talla10 = models.DecimalField('Talla 10', max_digits=11, decimal_places=2, null=True, blank=True)
    mvi_talla11 = models.DecimalField('Talla 11', max_digits=11, decimal_places=2, null=True, blank=True)
    mvi_talla12 = models.DecimalField('Talla 12', max_digits=11, decimal_places=2, null=True, blank=True)
    mvi_talla13 = models.DecimalField('Talla 13', max_digits=11, decimal_places=2, null=True, blank=True)

    mvi_kntidad = models.DecimalField('Cantidad Total', max_digits=11, decimal_places=2, null=True, blank=True)
    mvi_precios = models.DecimalField('Precio', max_digits=13, decimal_places=2, null=True, blank=True)
    mvi_desctos = models.DecimalField('Descuentos', max_digits=11, decimal_places=2, null=True, blank=True)
    mvi_rcargos = models.DecimalField('Recargos', max_digits=11, decimal_places=2, null=True, blank=True)
    mvi_deliver = models.DecimalField('Transporte', max_digits=11, decimal_places=2, null=True, blank=True)
    mvi_arancel = models.DecimalField('Aranceles', max_digits=11, decimal_places=2, null=True, blank=True)
    mvi_impuest = models.DecimalField('Impuestos IVA.', max_digits=11, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return str(self.mvi_nummovi)

    def save(self, commit=True, *args, **kwargs):
        # if self.id ?????:  ##   SOLO POR LA PRIMERA VEZ, LUEGO  SEGUIR  GRABANDO EL LMISMO NUMERO A TODOS LOS REG. DE LA MISMA TRANSACCION
        #     self.mvi_nummovi = "{0:0000007d}".format(
        #         self.mvi_nummovi.pk,  # 2
        #     )
        # TODO: Definir si amerita modificar los parámetros
        # TODO: Definir el max_length de CharField o poner TextField
        super(Movinvent, self).save(*args, **kwargs)
        # import pdb; pdb.set_trace()
        try:
            saldos = self.mvi_product.saldoxtalla
        except ObjectDoesNotExist:
            existencia = self.mvi_product
            comprom_actual = getattr(existencia, 'exs_comprom', None)
            existencia.exs_comprom = (comprom_actual or 0) + self.mvi_kntidad
            existencia.exs_dsponib = (existencia.exs_dsponib or 0) - existencia.exs_comprom
            existencia.save()
        else:
            # for num_talla in range(1, 14):
            #     egr_actual = getattr(saldos, "tex_egres{0:02d}".format(num_talla)) or 0
            #     egr_nuevo = egr_actual + getattr(self, "mvi_talla{0:02d}".format(num_talla)) or 0
            #     setattr(saldos, "tex_egres{0:02d}".format(num_talla), egr_nuevo)
            for num_talla in range(1, 14):
                cmp_actual = getattr(saldos, "tex_compr{0:02d}".format(num_talla)) or 0
                dsp_nuevo = cmp_actual + getattr(self, "mvi_talla{0:02d}".format(num_talla)) or 0
                setattr(saldos, "tex_dispo{0:02d}".format(num_talla), dsp_nuevo)
            saldos.save()


class Factura(models.Model):
    fac_idfactu = models.AutoField('Id. de Factura', primary_key=True)
    fac_ctrlfac = models.CharField('Núm. de Factura', max_length=12, editable=False)
    fac_npedido = models.ForeignKey(Pedido, verbose_name='Núm. de Pedido', null=True, blank=True)
    fac_fechfac = models.DateField('Fecha de la factura', default=timezone.now)
    fac_cajanum = models.ForeignKey(Caja, verbose_name='Núm. de caja', null=True, blank=True)
    fac_cajeras = models.ForeignKey(Cajera, verbose_name='Cód. de Cajera', null=True, blank=True)
    fac_cliente = models.ForeignKey(Cliente, verbose_name='Cód. de Cliente', null=True, blank=True)
    fac_vendedo = models.ForeignKey(Vendedor, verbose_name='Cód. de Vendedor', null=True, blank=True)
    fac_monedas = models.ForeignKey(Moneda, verbose_name='Núm. de Moneda', null=True, blank=True)
    fac_cotizac = models.DecimalField('Cotización', max_digits=9, decimal_places=2, null=True, blank=True)
    fac_totitms = models.DecimalField('Total de items', max_digits=15, decimal_places=2, null=True, blank=True)
    fac_totvlor = models.DecimalField('Total del valor', max_digits=15, decimal_places=2, null=True, blank=True)
    fac_totdsct = models.DecimalField('Total de descuentos', max_digits=15, decimal_places=2, null=True, blank=True)
    fac_totrkrg = models.DecimalField('Total de recaregos', max_digits=15, decimal_places=2, null=True, blank=True)
    fac_totflet = models.DecimalField('Total por deliver (transporte)', max_digits=15, decimal_places=2, null=True, blank=True)
    fac_totaran = models.DecimalField('Total aranceles', max_digits=15, decimal_places=2, null=True, blank=True)
    fac_tottaxs = models.DecimalField('Total taxes', max_digits=15, decimal_places=2, null=True, blank=True)
    fac_pgoefec = models.DecimalField('Cash', max_digits=15, decimal_places=2, null=True, blank=True)
    fac_pgocheq = models.DecimalField('Cheque', max_digits=15, decimal_places=2, null=True, blank=True)
    fac_pgotjcr = models.DecimalField('T./Crédito', max_digits=15, decimal_places=2, null=True, blank=True)
    fac_pgocred = models.DecimalField('Crédito personal', max_digits=15, decimal_places=2, null=True, blank=True)
    fac_otropgo = models.DecimalField('Internet (Paypal)', max_digits=15, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return str(self.fac_idfactu) if self.fac_idfactu else super(Factura, self).__str__()

    def save(self, *args, **kwargs):
        # if not self.id:
        # if 'request' in kwargs and self.user is None:
        # import pdb; pdb.set_trace()
        if 'request' in kwargs:
            request = kwargs.pop('request')
            if request:
                sucursal = request.user.sucursal
                # TODO: Validar en views que Sucursal de usuario esté activa y tenga Controlador
                controlador = Controlador.objects.get(ctl_sucrsal=sucursal)

                with transaction.atomic():
                    self.fac_ctrlfac = "{0:02d}{1:09d}".format(sucursal.id, controlador.ctl_secue01 + 1)
                    controlador.ctl_secue01 += 1
                    controlador.save()
                    super(Factura, self).save(*args, **kwargs)
        else:
            super(Factura, self).save(*args, **kwargs)
