from django import forms
from .models import Producto, Existencia, Saldoxtalla, Division, Marca, Modelo, Color, Tabtalla

class ProductoForm(forms.ModelForm):
	class Meta:
		model = Producto
#		exclude('prd_imgprod',)
		fields = [
			'prd_product',
			'prd_detalle',
			'prd_abrevia',
			'prd_tpoprod',
			'prd_tabtall',
			'prd_statreg', 
		]
		labels = {
			'prd_product': 'Código', 
			'prd_detalle': 'Detalle',
			'prd_abrevia': 'Abreviatura',
			'prd_tpoprod': 'Tipo de producto',
			'prd_tabtall': 'Tabla de Tallas',
			'prd_statreg': 'Status',
		}
		widgets = {
			'prd_product': forms.TextInput(),
			'prd_detalle': forms.TextInput(),
			'prd_abrevia': forms.TextInput(),
			'prd_tpoprod': forms.Select(),
			'prd_tabtall': forms.Select(),
#			'prd_statreg': forms.TextInput(),
		}

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
#			'div_statreg':  forms.BooleanInput(),
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
#			'mrk_statreg':  forms.TextInput(),
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
			'mod_idmodel':   'Código', #attrs={"class": "form_label"}
			'mod_idmarca':   'Marca',
			'mod_detalle':   'Detalle',
			'mod_abrevia':   'Abreviatura',
			'mod_tabtall':   'Cód./Tabla de Tallas',
			'mod_statreg':   'Status del Reg.',
		}

		widgets = {	
			'mod_idmodel':  forms.TextInput(attrs={"class": "form_widget"}),
			'mod_idmarca':  forms.Select(attrs={"class": "form_widget"}),
			'mod_detalle':  forms.TextInput(attrs={"class": "form_widget"}),
			'mod_abrevia':  forms.TextInput(attrs={"class": "form_widget"}),
			'mod_tabtall':  forms.Select(attrs={"class": "form_widget"}),
#			'mod_statreg':  forms.TextInput(),
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
#			'col_statreg':  forms.TextInput(),
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


class ExistenciaForm(forms.ModelForm):
	class Meta:
		model = Existencia
		fields = [	
#			'exs_sucursal',
			'exs_product',
			'exs_idunida',
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
			'exs_detalle',
			'exs_publico',
			'exs_special',

		]

		labels = {	
#			'exs_sucursal':   'Cód. de sucursal',
			'exs_product':   'Cód. Producto',
			'exs_idunida':   'Unid. De medida',
			'exs_saldinc':   'Saldo inicial',
			'exs_ingreso':   'Ingresos',
			'exs_egresos':   'Egresos',
			'exs_saldact':   'Saldo Actual',
			'exs_comprom':   'S.Compromet.(Ped. de Client)',
			'exs_xconfir':   'S. x confirm.(Ped.a Proveed)',
			'exs_dsponib':   'Saldo disponible',
			'exs_feching':   'Fecha de ult. Ingreso',
			'exs_fechegr':   'Fecha Ult. Egreso',
			'exs_fechinv':   'Fecha de inventario',
			'exs_costant':   'Costo promedio Anterior',
			'exs_dispant':   'Disponible Anterior',
			'exs_costact':   'Costo Actual',
			'exs_cosprom':   'Costo promedio Actual',
			'exs_distrib':	 'Precio:Distribuidos',
			'exs_mayoris':	 'Precio:Mayorista',
			'exs_detalle':	 'Precio:Detallista',
			'exs_publico':   'Precio:Publico',
			'exs_special':   'Precio:Especial',
		}

		widgets = {	
#			'exs_sucursal':  forms.TextInput(),
			'exs_product':  forms.TextInput(),
			'exs_idunida':  forms.TextInput(),
			'exs_saldinc':  forms.NumberInput(),
			'exs_ingreso':  forms.NumberInput(),
			'exs_egresos':  forms.NumberInput(),
			'exs_saldact':  forms.NumberInput(),
			'exs_comprom':  forms.NumberInput(),
			'exs_xconfir':  forms.NumberInput(),
			'exs_dsponib':  forms.NumberInput(),
			'exs_feching':  forms.DateInput(),
			'exs_fechegr':  forms.DateInput(),
			'exs_fechinv':  forms.DateInput(),
			'exs_costant':  forms.NumberInput(),
			'exs_dispant':  forms.NumberInput(),
			'exs_costact':  forms.NumberInput(),
			'exs_cosprom':  forms.NumberInput(),
			'exs_distrib':  forms.NumberInput(),
			'exs_mayoris':	forms.NumberInput(),
			'exs_detalle':	forms.NumberInput(),
			'exs_publico':	forms.NumberInput(),
			'exs_special':	forms.NumberInput(),
		}

class SaldoxtallaForm(forms.ModelForm):
	class Meta:
		model = Saldoxtalla
		fields = []	


