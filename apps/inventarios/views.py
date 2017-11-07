from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView
from .models import Division, Marca, Modelo, Color, Tabtalla, Producto, Existencia, Saldoxtalla, Productkey
from .forms import DivisionForm, MarcaForm, ModeloForm, ColorForm, TabtallaForm, ProductoForm, ExistenciaForm, SaldoxtallaForm, ProductkeyForm
#from apps.comercial.models import Cliente, Proveedor, Vendedor, Movinvent, Pedido, Factura
#from apps.finanzas.models import Caja, Cajera, Movicaja, Moneda
# {% extends 'base/base.html' %}

# Create your views here.


class DivLista(ListView):
	"""Listado de Division"""
	model = Division
	template_name = 'inventarios/Div_Panel.html'
	paginate_by = 8

class DivView(DetailView):
	"""Listado de Division"""
	template_name = 'inventarios/Div_View.html'
	model = Division

class DivNuevo(CreateView):
	"""Crear Division"""
	model = Division
	form_class = DivisionForm
	template_name = 'inventarios/Div_New.html'
	success_url = reverse_lazy('inventarios:div_panel')

class DivEdita(UpdateView):
	"""Listado de Divisions"""
	model = Division
	form_class = DivisionForm
	template_name = 'inventarios/Div_Edit.html'
	success_url = reverse_lazy('inventarios:div_panel')

class DivDelet(DeleteView):
	"""Listado de Divisions"""
	model = Division
	form_class = DivisionForm
	template_name = 'inventarios/Div_Delet.html'
	success_url = reverse_lazy('inventarios:div_panel')


#class MrkSelect(ListView):
#	"""Listado de Marca"""
#	model = Marca
#	template_name = 'inventarios/Prd_New.html'
#	context_object_name = 'slc_marcas'   ****--->> falta terminar para select-list dinamicas

class ProdkyLista(CreateView):
	model = Productkey
	form_class = ProductkeyForm
	template_name = 'inventarios/Exi_New.html'
	success_url = reverse_lazy('inventarios:exi_panel')

class Mrkkyselect(ListView):
	model = Marca
	template_name = 'inventarios/Prd_Select.html'
	context_object_name = 'all_marcas'
#	paginate_by = 10

# ========M A R C A S=========== #

class MrkLista(ListView):
	"""Listado de Marca"""
	model = Marca
	template_name = 'inventarios/Mrk_Panel.html'
	paginate_by = 8

class MrkView(DetailView):
	"""Listado de Marca"""
	template_name = 'inventarios/Mrk_View.html'
	model = Marca

class MrkNuevo(CreateView):
	"""Crear Marca"""
	model = Marca
	form_class = MarcaForm
	template_name = 'inventarios/Mrk_New.html'
	success_url = reverse_lazy('inventarios:mrk_panel')

class MrkEdita(UpdateView):
	"""Listado de Marcas"""
	model = Marca
	form_class = MarcaForm
	template_name = 'inventarios/Mrk_Edit.html'
	success_url = reverse_lazy('inventarios:mrk_panel')

class MrkDelet(DeleteView):
	"""Listado de Marcas"""
	model = Marca
	form_class = MarcaForm
	template_name = 'inventarios/Mrk_Delet.html'
	success_url = reverse_lazy('inventarios:mrk_panel')

	# ========M O  D  E  L  O  S=========== #

class ModLista(ListView):
	"""Listado de Modelo"""
	model = Modelo
	template_name = 'inventarios/Mod_Panel.html'
	paginate_by = 8

class ModView(DetailView):
	"""Listado de Modelo"""
	template_name = 'inventarios/Mod_View.html'
	model = Modelo

class ModNuevo(CreateView):
	"""Crear Modelo"""
	model = Modelo
	form_class = ModeloForm
	template_name = 'inventarios/Mod_New.html'
	success_url = reverse_lazy('inventarios:mod_panel')

class ModEdita(UpdateView):
	"""Listado de Modelos"""
	model = Modelo
	form_class = ModeloForm
	template_name = 'inventarios/Mod_Edit.html'
	success_url = reverse_lazy('inventarios:mod_panel')

class ModDelet(DeleteView):
	"""Listado de Modelos"""
	model = Modelo
	form_class = ModeloForm
	template_name = 'inventarios/Mod_Delet.html'
	success_url = reverse_lazy('inventarios:mod_panel')

# ======== C   O   L  O  R  E  S=========== #

class ColLista(ListView):
	"""Listado de Color"""
	model = Color
	template_name = 'inventarios/Col_Panel.html'
	paginate_by = 8

class ColView(DetailView):
	"""Listado de Color"""
	template_name = 'inventarios/Col_View.html'
	model = Color

class ColNuevo(CreateView):
	"""Crear Color"""
	model = Color
	form_class = ColorForm
	template_name = 'inventarios/Col_New.html'
	success_url = reverse_lazy('inventarios:col_panel')

class ColEdita(UpdateView):
	"""Listado de Colors"""
	model = Color
	form_class = ColorForm
	template_name = 'inventarios/Col_Edit.html'
	success_url = reverse_lazy('inventarios:col_panel')

class ColDelet(DeleteView):
	"""Listado de Colors"""
	model = Color
	form_class = ColorForm
	template_name = 'inventarios/Col_Delet.html'
	success_url = reverse_lazy('inventarios:col_panel')

# ======== T  A  B  T  A  L  L  A  S  =========== #

class TllLista(ListView):
	"""Listado de Tabtalla"""
	model = Tabtalla
	template_name = 'inventarios/Tll_Panel.html'
	paginate_by = 8

class TllView(DetailView):
	"""Listado de Tabtalla"""
	template_name = 'inventarios/Tll_View.html'
	model = Tabtalla

class TllNuevo(CreateView):
	"""Crear Tabtalla"""
	model = Tabtalla
	form_class = TabtallaForm
	template_name = 'inventarios/Tll_New.html'
	success_url = reverse_lazy('inventarios:tll_panel')

class TllEdita(UpdateView):
	"""Listado de Tabtallas"""
	model = Tabtalla
	form_class = TabtallaForm
	template_name = 'inventarios/Tll_Edit.html'
	success_url = reverse_lazy('inventarios:tll_panel')

class TllDelet(DeleteView):
	"""Listado de Tabtallas"""
	model = Tabtalla
	form_class = TabtallaForm
	template_name = 'inventarios/Tll_Delet.html'
	success_url = reverse_lazy('inventarios:tll_panel')


# ======== P  R  O  D  U  C  T  O  S  =========== #

class PrdLista(ListView):
	"""Listado de Producto"""
	model = Producto
	template_name = 'inventarios/Prd_Panel.html'
	paginate_by = 8

class PrdView(DetailView):
	"""Listado de Producto"""
	template_name = 'inventarios/Prd_View.html'
	model = Producto

class PrdNuevo(CreateView):
	"""Crear Producto"""
	model = Producto
	form_class = ProductoForm
	template_name = 'inventarios/Prd_New.html'
	success_url = reverse_lazy('inventarios:prd_panel')

class PrdEdita(UpdateView):
	"""Listado de Productos"""
	model = Producto
	form_class = ProductoForm
	template_name = 'inventarios/Prd_Edit.html'
	success_url = reverse_lazy('inventarios:prd_panel')

class PrdDelet(DeleteView):
	"""Listado de Productos"""
	model = Producto
	form_class = ProductoForm
	template_name = 'inventarios/Prd_Delet.html'
	success_url = reverse_lazy('inventarios:prd_panel')


# ======== E  X  I  S  T  E  N  C  I  A  S =========== #

class ExiLista(ListView):
	"""Listado de Existencia"""
	model = Existencia
	template_name = 'inventarios/Exi_Panel.html'
	paginate_by = 8

class ExiView(DetailView):
	"""Listado de Existencia"""
	template_name = 'inventarios/Exi_View.html'
	model = Existencia

class ExiNuevo(CreateView):
	"""Crear Existencia"""
	model = Existencia
	form_class = ExistenciaForm
	template_name = 'inventarios/Exi_New.html'
	success_url = reverse_lazy('inventarios:exi_panel')

class ExiEdita(UpdateView):
	"""Listado de Existencias"""
	model = Existencia
	form_class = ExistenciaForm
	template_name = 'inventarios/Exi_Edit.html'
	success_url = reverse_lazy('inventarios:exi_panel')

class ExiDelet(DeleteView):
	"""Listado de Existencias"""
	model = Existencia
	form_class = ExistenciaForm
	template_name = 'inventarios/Exi_Delet.html'
	success_url = reverse_lazy('inventarios:exi_panel')


# ======== SALDOS X TALLAS =========== #

class SxtLista(ListView):
	"""Listado de Saldoxtalla"""
	model = Saldoxtalla
	template_name = 'inventarios/Sxt_Panel.html'
	paginate_by = 8

class SxtView(DetailView):
	"""Listado de Saldoxtalla"""
	template_name = 'inventarios/Sxt_View.html'
	model = Saldoxtalla

class SxtNuevo(CreateView):
	"""Crear Saldoxtalla"""
	model = Saldoxtalla
	form_class = SaldoxtallaForm
	template_name = 'inventarios/Sxt_New.html'
	success_url = reverse_lazy('inventarios:sxt_panel')

class SxtEdita(UpdateView):
	"""Listado de Saldoxtallas"""
	model = Saldoxtalla
	form_class = SaldoxtallaForm
	template_name = 'inventarios/Sxt_Edit.html'
	success_url = reverse_lazy('inventarios:sxt_panel')

class SxtDelet(DeleteView):
	"""Listado de Saldoxtallas"""
	model = Saldoxtalla
	form_class = SaldoxtallaForm
	template_name = 'inventarios/Sxt_Delet.html'
	success_url = reverse_lazy('inventarios:sxt_panel')
