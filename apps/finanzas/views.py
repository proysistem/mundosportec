from django.shortcuts import render

# ======== M O N E D A S   =========== #

class MdaLista(ListView):
	"""Listado de Monedas"""
	model = Moneda
	template_name = 'finanzas/Mda_Panel.html'
	paginate_by = 8

class MdaView(DetailView):
	"""Visualiza reg. Moneda"""
	template_name = 'finanzas/Mda_View.html'
	model = Moneda

class MdaNuevo(CreateView):
	"""Crear Moneda"""
	model = Moneda
	form_class = MonedaForm
	template_name = 'finanzas/Mda_New.html'
	success_url = reverse_lazy('finanzas:mda_panel')

class MdaEdita(UpdateView):
	"""Actualiza Moneda"""
	model = Moneda
	form_class = MonedaForm
	template_name = 'finanzas/Mda_Edit.html'
	success_url = reverse_lazy('finanzas:mda_panel')

class MdaDelet(DeleteView):
	"""Elimina Moneda"""
	model = Moneda
	form_class = MonedaForm
	template_name = 'finanzas/Mda_Delet.html'
	success_url = reverse_lazy('finanzas:mda_panel')

# ======== C A J E R A  =========== #

class CjrLista(ListView):
	"""Listado de Cajeras"""
	model = Cajera
	template_name = 'finanzas/Cjr_Panel.html'
	paginate_by = 8

class CjrView(DetailView):
	"""Visualiza reg. Cajera"""
	template_name = 'finanzas/Cjr_View.html'
	model = Cajera

class CjrNuevo(CreateView):
	"""Crear Cajera"""
	model = Cajera
	form_class = CajeraForm
	template_name = 'finanzas/Cjr_New.html'
	success_url = reverse_lazy('finanzas:cjr_panel')

class CjrEdita(UpdateView):
	"""Actualiza Cajera"""
	model = Cajera
	form_class = CajeraForm
	template_name = 'finanzas/Cjr_Edit.html'
	success_url = reverse_lazy('finanzas:cjr_panel')

class CjrDelet(DeleteView):
	"""Elimina Cajera"""
	model = Cajera
	form_class = CajeraForm
	template_name = 'finanzas/Cjr_Delet.html'
	success_url = reverse_lazy('finanzas:cjr_panel')

# ======== C A J A  =========== #

class CjaLista(ListView):
	"""Listado de Cajas"""
	model = Caja
	template_name = 'finanzas/Cja_Panel.html'
	paginate_by = 8

class CjaView(DetailView):
	"""Visualiza reg. Caja"""
	template_name = 'finanzas/Cja_View.html'
	model = Caja

class CjaNuevo(CreateView):
	"""Crear Caja"""
	model = Caja
	form_class = CajaForm
	template_name = 'finanzas/Cja_New.html'
	success_url = reverse_lazy('finanzas:cja_panel')

class CjaEdita(UpdateView):
	"""Actualiza Caja"""
	model = Caja
	form_class = CajaForm
	template_name = 'finanzas/Cja_Edit.html'
	success_url = reverse_lazy('finanzas:cja_panel')

class CjaDelet(DeleteView):
	"""Elimina Caja"""
	model = Caja
	form_class = CajaForm
	template_name = 'finanzas/Cja_Delet.html'
	success_url = reverse_lazy('finanzas:cja_panel')

# ========    =========== #

class McjLista(ListView):
	"""Listado de Movicajas"""
	model = Movicaja
	template_name = 'finanzas/Mcj_Panel.html'
	paginate_by = 8

class McjView(DetailView):
	"""Visualiza reg. Movicaja"""
	template_name = 'finanzas/Mcj_View.html'
	model = Movicaja

class McjNuevo(CreateView):
	"""Crear Movicaja"""
	model = Movicaja
	form_class = MovicajaForm
	template_name = 'finanzas/Mcj_New.html'
	success_url = reverse_lazy('finanzas:mcj_panel')

class McjEdita(UpdateView):
	"""Actualiza Movicaja"""
	model = Movicaja
	form_class = MovicajaForm
	template_name = 'finanzas/Mcj_Edit.html'
	success_url = reverse_lazy('finanzas:mcj_panel')

class McjDelet(DeleteView):
	"""Elimina Movicaja"""
	model = Movicaja
	form_class = MovicajaForm
	template_name = 'finanzas/Mcj_Delet.html'
	success_url = reverse_lazy('finanzas:mcj_panel')

# ========    =========== #