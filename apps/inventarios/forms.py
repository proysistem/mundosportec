from django import forms
from .models import Existencia, Saldoxtalla, Division, Marca, Modelo, Color, Tabtalla
from django.utils.timezone import localtime, now
from decimal import Decimal


class DivisionForm(forms.ModelForm):
    class Meta:
        model = Division

        fields = [
            'div_detalle',
            'div_abrevia',
            'div_indicad',
            'div_statreg',
        ]

        labels = {
            'div_detalle':   'Detalle',
            'div_abrevia':   'Abreviatura',
            'div_indicad':   'Un indicador',
            'div_statreg':   'Status del Registro',
        }

        widgets = {
            'div_detalle':  forms.TextInput(),
            'div_abrevia':  forms.TextInput(),
            'div_indicad':  forms.NumberInput(),
            #  'div_statreg':  forms.BooleanInput(),
        }


class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca

        fields = [
            'mrk_idmarca',
            'mrk_detalle',
            'mrk_abrevia',
            'mrk_indicad',
            'mrk_statreg',
            ]

        labels = {
            'mrk_idmarca':   'Código',
            'mrk_detalle':   'Detalle',
            'mrk_abrevia':   'Abreviatura',
            'mrk_indicad':   'Indicador',
            'mrk_statreg':   'Status  del Registro',
        }

        widgets = {
            'mrk_idmarca':  forms.TextInput(),
            'mrk_detalle':  forms.TextInput(),
            'mrk_abrevia':  forms.TextInput(),
            'mrk_indicad':  forms.TextInput(),
#           'mrk_statreg':  forms.TextInput(),
        }



class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo

        fields = [
            'mod_idmodel',
            'mod_idmarca',
            'mod_detalle',
            'mod_abrevia',
            'mod_tabtall',
            'mod_statreg',
        ]

        labels = {
            'mod_idmodel':   'Código',  # attrs={"class": "form_label"}
            'mod_idmarca':   'Marca',
            'mod_detalle':   'Detalle',
            'mod_abrevia':   'Abreviatura',
            'mod_tabtall':   'Cód./Tabla de Tallas',
            'mod_statreg':   'Status del Reg.',
        }

        widgets = {
            'mod_idmodel':  forms.TextInput(attrs={"class": "form_widget", 'pattern': '[0-9]+'}),
            'mod_idmarca':  forms.Select(attrs={"class": "form_widget"}),
            'mod_detalle':  forms.TextInput(attrs={"class": "form_widget"}),
            'mod_abrevia':  forms.TextInput(attrs={"class": "form_widget"}),
            'mod_tabtall':  forms.Select(attrs={"class": "form_widget"}),
            # 'mod_statreg':  forms.TextInput(),
        }


class ColorForm(forms.ModelForm):
    class Meta:
        model = Color

        fields = [
            'col_idcolor',
            'col_detalle',
            'col_abrevia',
            'col_indicad',
            'col_statreg',
        ]

        labels = {
            'col_idcolor':   'Código',
            'col_detalle':   'Detalle',
            'col_abrevia':   'Abreviatura',
            'col_indicad':   'Indicador',
            'col_statreg':   'Status Reg.',
        }

        widgets = {
            'col_idcolor':  forms.TextInput(attrs={"class": "form_widget"}),
            'col_detalle':  forms.TextInput(attrs={"class": "form_widget"}),
            'col_abrevia':  forms.TextInput(attrs={"class": "form_widget"}),
            'col_indicad':  forms.TextInput(attrs={"class": "form_widget"}),
#           'col_statreg':  forms.TextInput(),
        }


class TabtallaForm(forms.ModelForm):
    class Meta:
        model = Tabtalla
        fields = [
            'jgo_idtalla',
            'jgo_divisio',
            'jgo_medid01',
            'jgo_medid02',
            'jgo_medid03',
            'jgo_medid04',
            'jgo_medid05',
            'jgo_medid06',
            'jgo_medid07',
            'jgo_medid08',
            'jgo_medid09',
            'jgo_medid10',
            'jgo_medid11',
            'jgo_medid12',
            'jgo_medid13',
        ]
        labels = {
            'jgo_idtalla':   'Cód.tabla de tallas',
            'jgo_divisio':   'Línea del producto',
            'jgo_medid01':   'Talla-01',
            'jgo_medid02':   'Talla-02',
            'jgo_medid03':   'Talla-03',
            'jgo_medid04':   'Talla-04',
            'jgo_medid05':   'Talla-05',
            'jgo_medid06':   'Talla-06',
            'jgo_medid07':   'Talla-07',
            'jgo_medid08':   'Talla-08',
            'jgo_medid09':   'Talla-09',
            'jgo_medid10':   'Talla-10',
            'jgo_medid11':   'Talla-11',
            'jgo_medid12':   'Talla-12',
            'jgo_medid13':   'Talla-13',
        }
        widgets = {
            'jgo_idtalla':  forms.TextInput(attrs={"class": "form_widget"}),
            'jgo_divisio':  forms.Select(attrs={"class": "form_widget"}),
            'jgo_medid01':  forms.TextInput(attrs={"class": "columns_tab_tall"}),
            'jgo_medid02':  forms.TextInput(attrs={"class": "columns_tab_tall"}),
            'jgo_medid03':  forms.TextInput(attrs={"class": "columns_tab_tall"}),
            'jgo_medid04':  forms.TextInput(attrs={"class": "columns_tab_tall"}),
            'jgo_medid05':  forms.TextInput(attrs={"class": "columns_tab_tall"}),
            'jgo_medid06':  forms.TextInput(attrs={"class": "columns_tab_tall"}),
            'jgo_medid07':  forms.TextInput(attrs={"class": "columns_tab_tall"}),
            'jgo_medid08':  forms.TextInput(attrs={"class": "columns_tab_tall"}),
            'jgo_medid09':  forms.TextInput(attrs={"class": "columns_tab_tall"}),
            'jgo_medid10':  forms.TextInput(attrs={"class": "columns_tab_tall"}),
            'jgo_medid11':  forms.TextInput(attrs={"class": "columns_tab_tall"}),
            'jgo_medid12':  forms.TextInput(attrs={"class": "columns_tab_tall"}),
            'jgo_medid13':  forms.TextInput(attrs={"class": "columns_tab_tall"}),
        }


class ExistenciaEditForm(forms.ModelForm):

    tex_inici01 = forms.DecimalField(required=False)
    tex_inici02 = forms.DecimalField(required=False)
    tex_inici03 = forms.DecimalField(required=False)
    tex_inici04 = forms.DecimalField(required=False)
    tex_inici05 = forms.DecimalField(required=False)
    tex_inici06 = forms.DecimalField(required=False)
    tex_inici07 = forms.DecimalField(required=False)
    tex_inici08 = forms.DecimalField(required=False)
    tex_inici09 = forms.DecimalField(required=False)
    tex_inici10 = forms.DecimalField(required=False)
    tex_inici11 = forms.DecimalField(required=False)
    tex_inici12 = forms.DecimalField(required=False)
    tex_inici13 = forms.DecimalField(required=False)
    tex_ingre01 = forms.DecimalField(required=False)
    tex_ingre02 = forms.DecimalField(required=False)
    tex_ingre03 = forms.DecimalField(required=False)
    tex_ingre04 = forms.DecimalField(required=False)
    tex_ingre05 = forms.DecimalField(required=False)
    tex_ingre06 = forms.DecimalField(required=False)
    tex_ingre07 = forms.DecimalField(required=False)
    tex_ingre08 = forms.DecimalField(required=False)
    tex_ingre09 = forms.DecimalField(required=False)
    tex_ingre10 = forms.DecimalField(required=False)
    tex_ingre11 = forms.DecimalField(required=False)
    tex_ingre12 = forms.DecimalField(required=False)
    tex_ingre13 = forms.DecimalField(required=False)
    tex_egres01 = forms.DecimalField(required=False)
    tex_egres02 = forms.DecimalField(required=False)
    tex_egres03 = forms.DecimalField(required=False)
    tex_egres04 = forms.DecimalField(required=False)
    tex_egres05 = forms.DecimalField(required=False)
    tex_egres06 = forms.DecimalField(required=False)
    tex_egres07 = forms.DecimalField(required=False)
    tex_egres08 = forms.DecimalField(required=False)
    tex_egres09 = forms.DecimalField(required=False)
    tex_egres10 = forms.DecimalField(required=False)
    tex_egres11 = forms.DecimalField(required=False)
    tex_egres12 = forms.DecimalField(required=False)
    tex_egres13 = forms.DecimalField(required=False)
    tex_compr01 = forms.DecimalField(required=False)
    tex_compr02 = forms.DecimalField(required=False)
    tex_compr03 = forms.DecimalField(required=False)
    tex_compr04 = forms.DecimalField(required=False)
    tex_compr05 = forms.DecimalField(required=False)
    tex_compr06 = forms.DecimalField(required=False)
    tex_compr07 = forms.DecimalField(required=False)
    tex_compr08 = forms.DecimalField(required=False)
    tex_compr09 = forms.DecimalField(required=False)
    tex_compr10 = forms.DecimalField(required=False)
    tex_compr11 = forms.DecimalField(required=False)
    tex_compr12 = forms.DecimalField(required=False)
    tex_compr13 = forms.DecimalField(required=False)
    exs_saldinc = forms.DecimalField(
        label="Saldo.inicial",
        required=False,
        decimal_places=2,
        max_digits=8,
        widget=forms.NumberInput(
            attrs={
                "disabled": "disabled",
                "step": "0.01"
            }),)

    # field = forms.DecimalField(label="Etiqueta", widget=)

    def __init__(self, *args, **kwargs):
        if 'instance' in kwargs:
            kwargs['instance'].exs_saldinc = kwargs['instance'].exs_saldinc.quantize(Decimal('0.01'))
            # TODO: Quantize all Decimal Fields
        super(ExistenciaEditForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Existencia
        fields = [
            "exs_sucursa",
            "exs_iddivis",
            "exs_idmarca",
            "exs_idmodel",
            "exs_idcolor",
            #'exs_product':
            #'exs_detalle',
            #'exs_abrevia',
            'exs_tpoprod',
            'exs_idunida',
            #'exs_tabtall',
            'exs_saldinc',
            'exs_ingreso',
            'exs_egresos',
            'exs_saldact',
            'exs_comprom',
            'exs_xconfir',
            'exs_dsponib',
            'exs_feching',
            'exs_fechegr',
            'exs_fechinv',
            'exs_costant',
            'exs_dispant',
            'exs_costact',
            'exs_cosprom',
            'exs_distrib',
            'exs_mayoris',
            'exs_detalls',
            'exs_publico',
            'exs_special',
            'exs_imgprod',
            'exs_statreg',

        ]

        labels = {
            "exs_sucursa":   'Sucursal',
            "exs_iddivis":   'Línea de productos',
            "exs_idmarca":   'Marca',
            "exs_idmodel":   'Modelo',
            "exs_idcolor":   'Color',
            # 'exs_product':   'Cód. Producto',
            # 'exs_detalle':   'Detalle',
            # 'exs_abrevia':   'Abreviatura',
            'exs_tpoprod':   'Tipo de producto',
            'exs_idunida':   'Unid. De medida',
            #'exs_tabtall':   'Tab./Tallas ',
            'exs_saldinc':   'Saldo.inicial',
            'exs_ingreso':   'Ingresos',
            'exs_egresos':   'Egresos',
            'exs_saldact':   'Saldo.Actual',
            'exs_comprom':   'S.Comprometido',
            'exs_xconfir':   'Sldo.x/confirmar',
            'exs_dsponib':   'Saldo.disponible',
            'exs_feching':   'Fecha/últ.Ingreso',
            'exs_fechegr':   'Fecha/últ.Egreso',
            'exs_fechinv':   'Fecha de inventario',
            'exs_costant':   'Costo.promedio.Anterior',
            'exs_dispant':   'Disponible.Anterior',
            'exs_costact':   'Costo Actual',
            'exs_cosprom':   'Cost.promed.Actual',
            'exs_distrib':   'Precio:Distribuidos',
            'exs_mayoris':   'Precio:Mayorista',
            'exs_detalls':   'Precio:Detallista',
            'exs_publico':   'Precio:Publico',
            'exs_special':   'Precio:Especial',
            'exs_imgprod':   'Imagen del producto',
            'exs_statreg':   'Status del reg.',
        }
        widgets = {
            "tex_ingre01":  forms.NumberInput(attrs={"disabled": "disabled"}),
            "exs_sucursa":  forms.Select(),
            "exs_iddivis":  forms.Select(),
            "exs_idmarca":  forms.Select(),
            "exs_idmodel":  forms.Select(),
            "exs_idcolor":  forms.Select(),
            # 'exs_product':   'Cód. Producto',
            # 'exs_detalle':  forms.TextInput(),
            # 'exs_abrevia':  forms.TextInput(),
            'exs_tpoprod':  forms.Select(),
            'exs_idunida':  forms.Select(),
            #'exs_tabtall':  forms.TextInput(),
            'exs_saldinc':  forms.NumberInput(attrs={"disabled": "disabled", "step": "0.01"}),
            'exs_ingreso':  forms.NumberInput(attrs={"disabled": "disabled"}),
            'exs_egresos':  forms.NumberInput(attrs={"disabled": "disabled"}),
            'exs_saldact':  forms.NumberInput(attrs={"disabled": "disabled"}),
            'exs_comprom':  forms.NumberInput(attrs={"disabled": "disabled"}),
            'exs_xconfir':  forms.NumberInput(attrs={"disabled": "disabled"}),
            'exs_dsponib':  forms.NumberInput(attrs={"disabled": "disabled"}),
            'exs_feching':  forms.DateInput(attrs={"disabled": "disabled"}),
            'exs_fechegr':  forms.DateInput(attrs={"disabled": "disabled"}),
            'exs_fechinv':  forms.DateInput(attrs={"disabled": "disabled"}),
            'exs_costant':  forms.NumberInput(),
            'exs_dispant':  forms.NumberInput(),
            'exs_costact':  forms.NumberInput(),
            'exs_cosprom':  forms.NumberInput(),
            'exs_distrib':  forms.NumberInput(),
            'exs_mayoris':  forms.NumberInput(),
            'exs_detalls':  forms.NumberInput(),
            'exs_publico':  forms.NumberInput(),
            'exs_special':  forms.NumberInput(),
            'exs_imgprod':  forms.ClearableFileInput(),
            # 'exs_statreg':  forms.BoleanInput(),
        }

    def save(self, commit=True):
        instance = super(ExistenciaEditForm, self).save(commit=False)
        sxt = Saldoxtalla(
            tex_product=instance,
            tex_inici01=self.cleaned_data['tex_inici01'],
            tex_inici02=self.cleaned_data['tex_inici02'],
            tex_inici03=self.cleaned_data['tex_inici03'],
            tex_inici04=self.cleaned_data['tex_inici04'],
            tex_inici05=self.cleaned_data['tex_inici05'],
            tex_inici06=self.cleaned_data['tex_inici06'],
            tex_inici07=self.cleaned_data['tex_inici07'],
            tex_inici08=self.cleaned_data['tex_inici08'],
            tex_inici09=self.cleaned_data['tex_inici09'],
            tex_inici10=self.cleaned_data['tex_inici10'],
            tex_inici11=self.cleaned_data['tex_inici11'],
            tex_inici12=self.cleaned_data['tex_inici12'],
            tex_inici13=self.cleaned_data['tex_inici13'],

            tex_ingre01=self.cleaned_data['tex_ingre01'],
            tex_ingre02=self.cleaned_data['tex_ingre02'],
            tex_ingre03=self.cleaned_data['tex_ingre03'],
            tex_ingre04=self.cleaned_data['tex_ingre04'],
            tex_ingre05=self.cleaned_data['tex_ingre05'],
            tex_ingre06=self.cleaned_data['tex_ingre06'],
            tex_ingre07=self.cleaned_data['tex_ingre07'],
            tex_ingre08=self.cleaned_data['tex_ingre08'],
            tex_ingre09=self.cleaned_data['tex_ingre09'],
            tex_ingre10=self.cleaned_data['tex_ingre10'],
            tex_ingre11=self.cleaned_data['tex_ingre11'],
            tex_ingre12=self.cleaned_data['tex_ingre12'],
            tex_ingre13=self.cleaned_data['tex_ingre13'],

            tex_egres01=self.cleaned_data['tex_egres01'],
            tex_egres02=self.cleaned_data['tex_egres02'],
            tex_egres03=self.cleaned_data['tex_egres03'],
            tex_egres04=self.cleaned_data['tex_egres04'],
            tex_egres05=self.cleaned_data['tex_egres05'],
            tex_egres06=self.cleaned_data['tex_egres06'],
            tex_egres07=self.cleaned_data['tex_egres07'],
            tex_egres08=self.cleaned_data['tex_egres08'],
            tex_egres09=self.cleaned_data['tex_egres09'],
            tex_egres10=self.cleaned_data['tex_egres10'],
            tex_egres11=self.cleaned_data['tex_egres11'],
            tex_egres12=self.cleaned_data['tex_egres12'],
            tex_egres13=self.cleaned_data['tex_egres13'],

            tex_compr01=self.cleaned_data['tex_compr01'],
            tex_compr02=self.cleaned_data['tex_compr02'],
            tex_compr03=self.cleaned_data['tex_compr03'],
            tex_compr04=self.cleaned_data['tex_compr04'],
            tex_compr05=self.cleaned_data['tex_compr05'],
            tex_compr06=self.cleaned_data['tex_compr06'],
            tex_compr07=self.cleaned_data['tex_compr07'],
            tex_compr08=self.cleaned_data['tex_compr08'],
            tex_compr09=self.cleaned_data['tex_compr09'],
            tex_compr10=self.cleaned_data['tex_compr10'],
            tex_compr11=self.cleaned_data['tex_compr11'],
            tex_compr12=self.cleaned_data['tex_compr12'],
            tex_compr13=self.cleaned_data['tex_compr13']
        )
        sxt.save(commit)

        if commit:
            instance.save()
        return instance


class ExistenciaForm(forms.ModelForm):
    exs_feching = forms.DateField(
        initial=localtime(now()).date(),
        widget=forms.DateInput(attrs={"type": "date"}, format='%Y-%m-%d',)
    )
    exs_fechegr = forms.DateField(
        initial=localtime(now()).date(),

        widget=forms.DateInput(attrs={"type": "date"}, format='%Y-%m-%d',)
    )
    exs_fechinv = forms.DateField(
        initial=localtime(now()).date(),
        widget=forms.DateInput(attrs={"type": "date"}, format='%Y-%m-%d',)
    )
    class Meta:
        model = Existencia
        fields = [
            "exs_sucursa",
            "exs_iddivis",
            "exs_idmarca",
            "exs_idmodel",
            "exs_idcolor",
            #'exs_product':
            #'exs_detalle',
            #'exs_abrevia',
            'exs_tpoprod',
            'exs_idunida',
            #'exs_tabtall',
            'exs_saldinc',
            'exs_ingreso',
            'exs_egresos',
            'exs_saldact',
            'exs_comprom',
            'exs_xconfir',
            'exs_dsponib',
            'exs_feching',
            'exs_fechegr',
            'exs_fechinv',
            'exs_costant',
            'exs_dispant',
            'exs_costact',
            'exs_cosprom',
            'exs_distrib',
            'exs_mayoris',
            'exs_detalls',
            'exs_publico',
            'exs_special',
            'exs_imgprod',
            'exs_statreg',

        ]

        labels = {
            "exs_sucursa":   'Sucursal',
            "exs_iddivis":   'Línea de productos',
            "exs_idmarca":   'Marca',
            "exs_idmodel":   'Modelo',
            "exs_idcolor":   'Color',
            # 'exs_product':   'Cód. Producto',
            # 'exs_detalle':   'Detalle',
            # 'exs_abrevia':   'Abreviatura',
            'exs_tpoprod':   'Tipo de producto',
            'exs_idunida':   'Unid. De medida',
            #'exs_tabtall':   'Tab./Tallas ',
            'exs_saldinc':   'Saldo.inicial',
            'exs_ingreso':   'Ingresos',
            'exs_egresos':   'Egresos',
            'exs_saldact':   'Saldo.Actual',
            'exs_comprom':   'S.Comprometido',
            'exs_xconfir':   'Sldo.x/confirmar',
            'exs_dsponib':   'Saldo.disponible',
            'exs_feching':   'Fecha/últ.Ingreso',
            'exs_fechegr':   'Fecha/últ.Egreso',
            'exs_fechinv':   'Fecha de inventario',
            'exs_costant':   'Costo.promedio.Anterior',
            'exs_dispant':   'Disponible.Anterior',
            'exs_costact':   'Costo Actual',
            'exs_cosprom':   'Costo promed.Actual',
            'exs_distrib':   'Precio:Distribuidos',
            'exs_mayoris':   'Precio:Mayorista',
            'exs_detalls':   'Precio:Detallista',
            'exs_publico':   'Precio:Publico',
            'exs_special':   'Precio:Especial',
            'exs_imgprod':   'Imagen del producto',
            'exs_statreg':   'Status del reg.',
        }

        widgets = {
            "exs_sucursa":  forms.Select(),
            "exs_iddivis":  forms.Select(),
            "exs_idmarca":  forms.Select(),
            "exs_idmodel":  forms.Select(),
            "exs_idcolor":  forms.Select(),
            # 'exs_product':   'Cód. Producto',
            # 'exs_detalle':  forms.TextInput(),
            # 'exs_abrevia':  forms.TextInput(),
            'exs_tpoprod':  forms.Select(),
            'exs_idunida':  forms.Select(),
            #'exs_tabtall':  forms.TextInput(),
            'exs_saldinc':  forms.NumberInput(),
            'exs_ingreso':  forms.NumberInput(),
            'exs_egresos':  forms.NumberInput(),
            'exs_saldact':  forms.NumberInput(),
            'exs_comprom':  forms.NumberInput(),
            'exs_xconfir':  forms.NumberInput(),
            'exs_dsponib':  forms.NumberInput(),
#            'exs_feching':  forms.DateInput(attrs={"type": "date"}),
#            'exs_fechegr':  forms.DateInput(attrs={"type": "date"}),
#            'exs_fechinv':  forms.DateInput(attrs={"type": "date"}),
            'exs_costant':  forms.NumberInput(),
            'exs_dispant':  forms.NumberInput(),
            'exs_costact':  forms.NumberInput(),
            'exs_cosprom':  forms.NumberInput(),
            'exs_distrib':  forms.NumberInput(),
            'exs_mayoris':  forms.NumberInput(),
            'exs_detalls':  forms.NumberInput(),
            'exs_publico':  forms.NumberInput(),
            'exs_special':  forms.NumberInput(),
            'exs_imgprod':  forms.FileInput(),
#           'exs_statreg':  forms.BoleanInput(),
        }


class SaldoxtallaForm(forms.ModelForm):
    class Meta:
        model = Saldoxtalla
        exclude = ['id']
