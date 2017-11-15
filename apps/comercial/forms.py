from django import forms
from .models import Cliente, Proveedor, Vendedor, Movinvent, Pedido, Factura
from django.utils.timezone import localtime, now


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente

        fields = [
                'clt_frsname',
                'clt_midname',
                'clt_secmane',
                'clt_fechnac',
                'clt_direcci',
                'clt_ciudade',
                'clt_estados',
                'cli_country',
                'clt_zipcodg',
                'clt_telefon',
                'clt_celular',
                'clt_correoe',
                'clt_imgclte',
                'clt_rgunico',
                'clt_categor',
                ]
        labels = {
                'clt_frsname':  'Primer Nombre',
                'clt_midname':  'Segundo Nombre',
                'clt_secmane':  'Apellidos',
                'clt_fechnac':  'Fecha de Nacimiento',
                'clt_direcci':  'Dirección',
                'clt_ciudade':  'Ciudad',
                'clt_estados':  'Provincia',
                'cli_country':  'Pais',
                'clt_zipcodg':  'Cód. Postal',
                'clt_telefon':  'Núm. de telefono',
                'clt_celular':  'Núm. de Celular',
                'clt_correoe':  'E-mail',
                'clt_imgclte':  'Foto de Clte.',
                'clt_rgunico':  'Reg. único',
                'clt_categor':  'Categoría',
                }
        widgets = {
                'clt_frsname': forms.TextInput(),
                'clt_midname': forms.TextInput(),
                'clt_secmane': forms.TextInput(),
                'clt_fechnac': forms.DateInput(attrs={"type": "date"}),
                'clt_direcci': forms.Select(),
                'clt_ciudade': forms.Select(),
                'clt_estados': forms.Select(),
                'cli_country': forms.Select(),
                'clt_zipcodg': forms.Select(),
                'clt_telefon': forms.NumberInput(),
                'clt_celular': forms.NumberInput(),
                'clt_correoe': forms.EmailInput(),
                # 'clt_imgclte': forms.NumberInput(),
                'clt_rgunico': forms.TextInput(),
                'clt_categor': forms.Select(),
                }


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = [
                'prv_frsname',
                'prv_midname',
                'prv_secmane',
                'prv_fechnac',
                'prv_direcci',
                'prv_ciudade',
                'prv_estados',
                'prv_country',
                'prv_zipcodg',
                'prv_telefon',
                'prv_celular',
                'prv_correoe',
                'prv_imgprov',
                'prv_rgunico',
                'prv_categor',

        ]
        labels = {

                'prv_frsname':  'Primer Nombre',
                'prv_midname':  'Segundo Nombre',
                'prv_secmane':  'Apellidos',
                'prv_fechnac':  'Fecha de Nacimiento',
                'prv_direcci':  'Dirección',
                'prv_ciudade':  'Ciudad',
                'prv_estados':  'Provincia',
                'prv_country':  'Pais',
                'prv_zipcodg':  'Cód. Postal',
                'prv_telefon':  'Núm. de telefono',
                'prv_celular':  'Núm. de Celular',
                'prv_correoe':  'E-mail',
                'prv_imgprov':  'Foto de Proveedor',
                'prv_rgunico':  'Reg. único',
                'prv_categor':  'Categoría',

        }
        widgets = {

                'prv_frsname': forms.TextInput(),
                'prv_midname': forms.TextInput(),
                'prv_secmane': forms.TextInput(),
                'prv_fechnac': forms.DateInput(attrs={"type": "date"}),
                'prv_direcci': forms.Select(),
                'prv_ciudade': forms.Select(),
                'prv_estados': forms.Select(),
                'prv_country': forms.Select(),
                'prv_zipcodg': forms.Select(),
                'prv_telefon': forms.NumberInput(),
                'prv_celular': forms.NumberInput(),
                'prv_correoe': forms.EmailInput(),
                # 'prv_imgprov': forms.NumberInput(),
                'prv_rgunico': forms.TextInput(),
                'prv_categor': forms.Select(),
        }


class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = [
                'vnd_frsname',
                'vnd_midname',
                'vnd_secmane',
                'vnd_fechnac',
                'vnd_direcci',
                'vnd_ciudade',
                'vnd_estados',
                'vnd_country',
                'vnd_zipcodg',
                'vnd_telefon',
                'vnd_ncelula',
                'vnd_correoe',
                'vnd_addrimg',
                'vnd_rgunico',
                'vnd_categor',

        ]
        labels = {

                'vnd_frsname':  'Primer Nombre',
                'vnd_midname':  'Segundo Nombre',
                'vnd_secmane':  'Apellidos',
                'vnd_fechnac':  'Fecha de Nacimiento',
                'vnd_direcci':  'Dirección',
                'vnd_ciudade':  'Ciudad',
                'vnd_estados':  'Provincia',
                'vnd_country':  'Pais',
                'vnd_zipcodg':  'Cód. Postal',
                'vnd_telefon':  'Núm. de telefono',
                'vnd_ncelula':  'Núm. de Celular',
                'vnd_correoe':  'E-mail',
                'vnd_addrimg':  'Foto del Vendedor',
                'vnd_rgunico':  'Reg. único',
                'vnd_categor':  'Categoría',

        }
        widgets = {

                'vnd_frsname': forms.TextInput(),
                'vnd_midname': forms.TextInput(),
                'vnd_secmane': forms.TextInput(),
                'vnd_fechnac': forms.DateInput(attrs={"type": "date"}),
                'vnd_direcci': forms.Select(),
                'vnd_ciudade': forms.Select(),
                'vnd_estados': forms.Select(),
                'vnd_country': forms.Select(),
                'vnd_zipcodg': forms.Select(),
                'vnd_telefon': forms.NumberInput(),
                'vnd_ncelula': forms.NumberInput(),
                'vnd_correoe': forms.EmailInput(),
                # 'vnd_addrimg': forms.NumberInput(),
                'vnd_rgunico': forms.TextInput(),
                'vnd_categor': forms.Select(),
                }


class MovinventForm(forms.ModelForm):

    class Meta:
        model = Movinvent
        fields = [

                'mvi_nummovi',
                'mvi_fechmov',
                'mvi_motivos',
                'mvi_pedidos',
                'mvi_factura',
                'mvi_tipomov',
                'mvi_vendedo',
                'mvi_cliente',
                'mvi_sucursa',
                'mvi_product',
                'mvi_unidade',
                'mvi_talla01',
                'mvi_talla02',
                'mvi_talla03',
                'mvi_talla04',
                'mvi_talla05',
                'mvi_talla06',
                'mvi_talla07',
                'mvi_talla08',
                'mvi_talla09',
                'mvi_talla10',
                'mvi_talla11',
                'mvi_talla12',
                'mvi_talla13',
                'mvi_kntidad',
                'mvi_precios',
                'mvi_desctos',
                'mvi_rcargos',
                'mvi_deliver',
                'mvi_arancel',
                'mvi_impuest',
        ]

        labels = {
                'mvi_nummovi':  'Núm.movimiento',
                'mvi_fechmov':  'Fecha',
                'mvi_motivos':  'Motivo',
                'mvi_pedidos':  'Núm.de pedido',
                'mvi_factura':  'Núm.de factura',
                'mvi_tipomov':  'Tipo/Movimiento',
                'mvi_vendedo':  'Vendedor',
                'mvi_cliente':  'Cliente',
                'mvi_sucursa':  'Sucursal',
                'mvi_product':  'Producto',
                'mvi_unidade':  'Unidad',
                'mvi_talla01':  'Talla 01',
                'mvi_talla02':  'Talla 02',
                'mvi_talla03':  'Talla 03',
                'mvi_talla04':  'Talla 04',
                'mvi_talla05':  'Talla 05',
                'mvi_talla06':  'Talla 06',
                'mvi_talla07':  'Talla 07',
                'mvi_talla08':  'Talla 08',
                'mvi_talla09':  'Talla 09',
                'mvi_talla10':  'Talla 10',
                'mvi_talla11':  'Talla 11',
                'mvi_talla12':  'Talla 12',
                'mvi_talla13':  'Talla 13',
                'mvi_kntidad':  'Cantidad',
                'mvi_precios':  'Precio',
                'mvi_desctos':  'Descuento',
                'mvi_rcargos':  'Recargos',
                'mvi_deliver':  'Transporte',
                'mvi_arancel':  'Aranceles',
                'mvi_impuest':  'Impuestos IVA',
        }
        widgets = {

                'mvi_nummovi':   forms.NumberInput(),
                'mvi_fechmov':   forms.DateInput(attrs={"type": "date"}),
                'mvi_motivos':   forms.Select(),
                'mvi_pedidos':   forms.NumberInput(),
                'mvi_factura':   forms.NumberInput(),
                'mvi_tipomov':   forms.Select(),
                'mvi_vendedo':   forms.Select(),
                'mvi_cliente':   forms.Select(),
                'mvi_sucursa':   forms.Select(),
                'mvi_product':   forms.Select(),
                'mvi_unidade':   forms.Select(),
                'mvi_talla01':   forms.TextInput(),
                'mvi_talla02':   forms.TextInput(),
                'mvi_talla03':   forms.TextInput(),
                'mvi_talla04':   forms.TextInput(),
                'mvi_talla05':   forms.TextInput(),
                'mvi_talla06':   forms.TextInput(),
                'mvi_talla07':   forms.TextInput(),
                'mvi_talla08':   forms.TextInput(),
                'mvi_talla09':   forms.TextInput(),
                'mvi_talla10':   forms.TextInput(),
                'mvi_talla11':   forms.TextInput(),
                'mvi_talla12':   forms.TextInput(),
                'mvi_talla13':   forms.TextInput(),
                'mvi_kntidad':   forms.NumberInput(),
                'mvi_precios':   forms.NumberInput(),
                'mvi_desctos':   forms.NumberInput(),
                'mvi_rcargos':   forms.NumberInput(),
                'mvi_deliver':   forms.NumberInput(),
                'mvi_arancel':   forms.NumberInput(),
                'mvi_impuest':   forms.NumberInput(),

        }


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [

                'Ped_motivos',
                'ped_mvinven',
                'ped_fechfac',
                'ped_cajanum',
                'ped_cajeras',
                'ped_cliente',
                'ped_vendedo',
                # 'ped_factura',
                'ped_totitms',
                'ped_totvlor',
                'ped_totdsct',
                'ped_totrkrg',
                'ped_totflet',
                'ped_totaran',
                'ped_tottaxs',
        ]

        labels = {
                'Ped_motivos':  'Fecha',
                'ped_mvinven':  'Motivo',
                'ped_fechfac':  'Núm.de pedido',
                'ped_cajanum':  'Núm.de factura',
                'ped_cajeras':  'Tipo/Movimiento',
                'ped_cliente':  'Vendedor',
                'ped_vendedo':  'Cliente',
                # 'ped_factura':  'Sucursal',
                'ped_totitms':  'Producto',
                'ped_totvlor':  'Unidad',
                'ped_totdsct':  'Talla 01',
                'ped_totrkrg':  'Talla 02',
                'ped_totflet':  'Talla 03',
                'ped_totaran':  'Talla 04',
                'ped_tottaxs':  'Talla 05',
        }
        widgets = {

                'Ped_motivos':   forms.Select(),
                'ped_mvinven':   forms.Select(),
                'ped_fechfac':   forms.DateInput(attrs={"type": "date"}),
                'ped_cajanum':   forms.Select(),
                'ped_cajeras':   forms.Select(),
                'ped_cliente':   forms.Select(),
                'ped_vendedo':   forms.Select(),
                # 'ped_factura':   forms.Select(),
                'ped_totitms':   forms.NumberInput(),
                'ped_totvlor':   forms.NumberInput(),
                'ped_totdsct':   forms.NumberInput(),
                'ped_totrkrg':   forms.NumberInput(),
                'ped_totflet':   forms.NumberInput(),
                'ped_totaran':   forms.NumberInput(),
                'ped_tottaxs':   forms.NumberInput(),
                }


class FacturaForm(forms.ModelForm):
    fac_fechfac = forms.DateField(initial=localtime(now()).date())
    # TODO:
    # - Create Inline form form with these fields:
    #   Product, Detail (? is this writable?), Quantity, Unit, Price, Discount, IVA, Value

    class Meta:
        model = Factura
        fields = [
                'fac_idfactu',
                'fac_fechfac',
                'fac_cajanum',
                'fac_cajeras',
                'fac_cliente',
                'fac_vendedo',
                'fac_pedidos',
                'fac_monedas',
                'fac_cotizac',
                'fac_totitms',
                'fac_totvlor',
                'fac_totdsct',
                'fac_totrkrg',
                'fac_totflet',
                'fac_totaran',
                'fac_tottaxs',
                'fac_pgoefec',
                'fac_pgocheq',
                'fac_pgotjcr',
                'fac_pgocred',
                'fac_otropgo',
        ]

        labels = {

                'fac_idfactu':  'Núm. de Factura',
                'fac_fechfac':  'Fecha de Factura',
                'fac_cajanum':  'Núm. de Caja',
                'fac_cajeras':  'Cajer@',
                'fac_cliente':  'Cliente',
                'fac_vendedo':  'Vendedor',
                'fac_pedidos':  'Núm. de pedido',
                'fac_monedas':  'Moneda',
                'fac_cotizac':  'Cotización',
                'fac_totitms':  'Items',
                'fac_totvlor':  'Total Valor',
                'fac_totdsct':  'Total Descuentos',
                'fac_totrkrg':  'Totla de Recargos',
                'fac_totflet':  'Total de Flete',
                'fac_totaran':  'Total Aranceles',
                'fac_tottaxs':  'Total IVA',
                'fac_pgoefec':  'Efectivo',
                'fac_pgocheq':  'Cheques',
                'fac_pgotjcr':  'Tarj./Crédito',
                'fac_pgocred':  'Crédit.Personal',
                'fac_otropgo':  'Otra forma',
        }
        widgets = {
                # fac_idfactu':  NumberInput(),
                'fac_fechfac':  forms.DateInput(attrs={"type": "date"}),
                'fac_cajanum':  forms.Select(),
                'fac_cajeras':  forms.Select(),
                'fac_cliente':  forms.Select(),
                'fac_vendedo':  forms.Select(),
                'fac_pedidos':  forms.Select(),
                'fac_monedas':  forms.Select(),
                'fac_cotizac':  forms.NumberInput(),
                'fac_totitms':  forms.NumberInput(),
                'fac_totvlor':  forms.NumberInput(),
                'fac_totdsct':  forms.NumberInput(),
                'fac_totrkrg':  forms.NumberInput(),
                'fac_totflet':  forms.NumberInput(),
                'fac_totaran':  forms.NumberInput(),
                'fac_tottaxs':  forms.NumberInput(),
                'fac_pgoefec':  forms.NumberInput(),
                'fac_pgocheq':  forms.NumberInput(),
                'fac_pgotjcr':  forms.NumberInput(),
                'fac_pgocred':  forms.NumberInput(),
                'fac_otropgo':  forms.NumberInput(),
        }
