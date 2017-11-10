from django.db import models
from apps.finanzas.models import Cajera, Caja, Moneda
from apps.inventarios.models import Existencia, Unidad
from apps.parametros.models import Pais, Provincia, Ciudad, Zipcodigo, Sucursal, Tipomovim, Motivo, Categoria


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
    clt_rgunico = models.IntegerField('Registro Unico', max_length=20, blank=True)
    clt_categor = models.ForeignKey(Categoria, null=True, blank=True)


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
    prv_rgunico = models.IntegerField('Registro Unico', max_length=20,, blank=True)
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
    vnd_rgunico = models.IntegerField('Registro Unico' max_length=20, blank=True)
    vnd_categor = models.ForeignKey(Categoria, null=True, blank=True)

class Movinvent(models.Model):

    mvi_nummovi = models.IntegerField('Núm. de movimiento', editable=False, null=True, blank=True)
    mvi_fechmov = models.DateField('Fecha')
    mvi_motivos = models.ForeignKey(Motivo)
    mvi_pedidos = models.IntegerField('Núm. de pedido', null=True, blank=True)
    mvi_factura = models.IntegerField('Núm. de factrura', null=True, blank=True)
    mvi_tipomov = models.ForeignKey(Tipomovim)
    mvi_vendedo = models.ForeignKey(Vendedor)
    mvi_cliente = models.ForeignKey(Cliente)
    mvi_sucursa = models.ForeignKey(Sucursal)
    mvi_product = models.ForeignKey(Existencia)
    mvi_unidade = models.ForeignKey(Unidad)
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
    mvi_kntidad = models.DecimalField('Cantidad Total', max_digits=11, decimal_places=4, null=True, blank=True)
    mvi_precios = models.DecimalField('Precio', max_digits=13, decimal_places=4, null=True, blank=True)
    mvi_desctos = models.DecimalField('Descuentos', max_digits=11, decimal_places=4, null=True, blank=True)
    mvi_rcargos = models.DecimalField('Recargos', max_digits=11, decimal_places=4, null=True, blank=True)
    mvi_deliver = models.DecimalField('Transporte', max_digits=11, decimal_places=4, null=True, blank=True)
    mvi_arancel = models.DecimalField('Aranceles', max_digits=11, decimal_places=4, null=True, blank=True)
    mvi_impuest = models.DecimalField('Impuestos IVA.', max_digits=11, decimal_places=4, null=True, blank=True)
    def __str__(self):
        return (self.mvi_nummovi)

    def save(self, *args, **kwargs):
        if self.id ?????:  ##   SOLO POR LA PRIMERA VEZ, LUEGO  SEGUIR  GRABANDO EL LMISMO NUMERO A TODOS LOS REG. DE LA MISMA TRANSACCION
            self.mvi_nummovi = "{0:0000007d}".format(
                self.mvi_nummovi.pk,  # 2
            )
        # TODO: Definir si amerita modificar los parámetros
        # TODO: Definir el max_length de CharField o poner TextField
        super(Existencia, self).save()



class Pedido(models.Model):

    Ped_motivos = models.ForeignKey(Motivo)
    ped_mvinven = models.ForeignKey(Movinvent)
    ped_fechfac = models.DateField('Fecha de pedido', )
    ped_cajanum = models.ForeignKey(Caja, null=True, blank=True)
    ped_cajeras = models.ForeignKey(Cajera, null=True, blank=True)
    ped_cliente = models.ForeignKey(Cliente)
    ped_vendedo = models.ForeignKey(Vendedor, null=True, blank=True)
#   ped_factura = models.ForeignKey(Factura, null=True, blank=True)
    ped_totitms = models.DecimalField('Total de items', max_digits=15, decimal_places=4, null=True, blank=True)
    ped_totvlor = models.DecimalField('Total del valor', max_digits=15, decimal_places=4, null=True, blank=True)
    ped_totdsct = models.DecimalField('Total de descuentos', max_digits=15, decimal_places=4, null=True, blank=True)
    ped_totrkrg = models.DecimalField('Total de regaregos', max_digits=15, decimal_places=4, null=True, blank=True)
    ped_totflet = models.DecimalField('Total por deliver (transporte)', max_digits=15, decimal_places=4, null=True, blank=True)
    ped_totaran = models.DecimalField('Total aranceles', max_digits=15, decimal_places=4, null=True, blank=True)
    ped_tottaxs = models.DecimalField('Total taxes', max_digits=15, decimal_places=4, null=True, blank=True)


class Factura(models.Model):

    fac_idfactu = models.IntegerField('Núm. de Factura')
    fac_mvinven = models.ForeignKey(Movinvent)
    fac_fechfac = models.DateField('fecha de la factura', )
    fac_cajanum = models.ForeignKey(Caja)
    fac_cajeras = models.ForeignKey(Cajera)
    fac_cliente = models.ForeignKey(Cliente)
    fac_vendedo = models.ForeignKey(Vendedor)
    fac_pedidos = models.ForeignKey(Pedido)
    fac_monedas = models.ForeignKey(Moneda)
    fac_cotizac = models.DecimalField('Cotización', max_digits=9, decimal_places=4, null=True, blank=True)
    fac_totitms = models.DecimalField('Total de items', max_digits=15, decimal_places=4, null=True, blank=True)
    fac_totvlor = models.DecimalField('Total del valor', max_digits=15, decimal_places=4, null=True, blank=True)
    fac_totdsct = models.DecimalField('Total de descuentos', max_digits=15, decimal_places=4, null=True, blank=True)
    fac_totrkrg = models.DecimalField('Total de recaregos', max_digits=15, decimal_places=4, null=True, blank=True)
    fac_totflet = models.DecimalField('Total por deliver (transporte)', max_digits=15, decimal_places=4, null=True, blank=True)
    fac_totaran = models.DecimalField('Total aranceles', max_digits=15, decimal_places=4, null=True, blank=True)
    fac_tottaxs = models.DecimalField('Total taxes', max_digits=15, decimal_places=4, null=True, blank=True)
    fac_pgoefec = models.DecimalField('Cash', max_digits=15, decimal_places=4, null=True, blank=True)
    fac_pgocheq = models.DecimalField('Cheque', max_digits=15, decimal_places=4, null=True, blank=True)
    fac_pgotjcr = models.DecimalField('T./Crédito', max_digits=15, decimal_places=4, null=True, blank=True)
    fac_pgocred = models.DecimalField('Crédito personal', max_digits=15, decimal_places=4, null=True, blank=True)
    fac_otropgo = models.DecimalField('Internet (Paypal)', max_digits=15, decimal_places=4, null=True, blank=True)
