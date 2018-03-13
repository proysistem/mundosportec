from django import forms
from apps.parametros.models import Sucursal, Zipcodigo, Pais, Provincia, Ciudad


class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = [

            'suc_codgsuc',
            'suc_nombres',
            'suc_abrevia',
            'suc_direcci',
            'suc_ciudads',
            'suc_estados',
            'suc_country',
            'suc_zipcodg',
            'suc_impuest',
            'suc_statreg',
        ]
        labels = {
            'suc_codgsuc': 'Cód. Sucursal',
            'suc_nombres': 'Nombre',
            'suc_abrevia': 'Abreviatura',
            'suc_direcci': 'Dirección',
            'suc_ciudads': 'Ciudad',
            'suc_estados': 'Provincia',
            'suc_country': 'País',
            'suc_zipcodg': 'Cód.Postal',
            'suc_impuest': 'I.V.A.',
            'suc_statreg': 'Status',
        }
        widgets = {
            'suc_codgsuc': forms.TextInput(),
            'suc_nombres': forms.TextInput(),
            'suc_abrevia': forms.TextInput(),
            'suc_direcci': forms.TextInput(),
            'suc_ciudads': forms.Select(),
            'suc_estados': forms.Select(),
            'suc_country': forms.Select(),
            'suc_zipcodg': forms.Select(),
            'suc_impuest': forms.NumberInput(),
            'suc_statreg': forms.TextInput(),
        }


class ZipcodigoForm(forms.ModelForm):
    class Meta:
        model = Zipcodigo
        fields = [
            'zip_idzipco',
            'zip_idciuda',
            'zip_estados',
            'zip_country',
        ]
        labels = {
            'zip_idzipco':   'Código Postal',
            'zip_idciuda':   'Ciudad',
            'zip_estados':   'Estado',
            'zip_country':   'País',
        }

        widgets = {
            'zip_idzipco':  forms.TextInput(),
            'zip_idciuda':  forms.Select(),
            'zip_estados':  forms.Select(),
            'zip_country':  forms.Select(),
        }


class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = [
            'ciu_estados',
            'ciu_country',
            'ciu_nombres',
            'ciu_abrevia',
        ]
        labels = {
            'ciu_country': 'Pais',
            'ciu_estados': 'Estados',
            'ciu_nombres': 'Nombre',
            'ciu_abrevia': 'Abreviatura',
        }

        widgets = {
            'ciu_country':  forms.Select(),
            'ciu_estados':  forms.Select(),
            'ciu_nombres':  forms.TextInput(),
            'ciu_abrevia':  forms.TextInput(),
        }


class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = [
            'pai_detalle',
            'pai_abrevia',
            ]
        labels = {
            'pai_detalle':  'País',
            'pai_abrevia':  'Abreviatura',

        }

        widgets = {
            'pai_detalle': forms.TextInput(),
            'pai_abrevia': forms.TextInput(),
        }


class ProvinciaForm(forms.ModelForm):
    class Meta:
        model = Provincia
        fields = [
            'est_country',
            'est_detalle',
            'est_abrevia',
            'est_capital',
        ]
        labels = {
            'est_country':     'País',
            'est_detalle':     'Provincia',
            'est_abrevia':    'Abreviatura',
            'est_capital':    'Capital',

        }

        widgets = {
            'est_country': forms.Select(),
            'est_detalle': forms.TextInput(),
            'est_abrevia': forms.TextInput(),
            'est_capital': forms.TextInput(),
        }
