# from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView
from .models import Zipcodigo, Sucursal, Ciudad, Provincia, Pais
from apps.parametros.forms import SucursalForm, ZipcodigoForm, CiudadForm, PaisForm, ProvinciaForm
from django.core.urlresolvers import reverse_lazy
# from django.http import HttpResponse

# Create your views here.


class SucursView(TemplateView):

    model = Sucursal
    template_name = 'parametros/pindex.html'

    def get_context_data(self, **kwargs):
        context = super(SucursView, self).get_context_data(**kwargs)
        context["var_sucursl"] = Sucursal.objects.all().order_by('suc_nombres')[:6]  # obtengo las 10 sucursales ordenadas por nombre
        context["var_zipcodg"] = Zipcodigo.objects.all()
        return context
#    return HttpResponse("Pindex")
# from .models import Pais, Provincia, Ciudad, Zipcodigo, Sucursal, Categoria, Tipomovim, Motivo


class SucLista(ListView):
    """Listado de Sucursales"""
    model = Sucursal
    template_name = 'parametros/Suc_Panel.html'
    paginate_by = 8


class SucNuevo(CreateView):
    """Crear Sucursales"""
    model = Sucursal
    form_class = SucursalForm
    template_name = 'parametros/Suc_New.html'
    success_url = reverse_lazy('parametros:suc_panel')


class SucView(DetailView):
    """Listado de Sucursales"""
    template_name = 'parametros/Suc_View.html'
    model = Sucursal


class SucEdita(UpdateView):
    """Listado de Sucursales"""
    model = Sucursal
    form_class = SucursalForm
    template_name = 'parametros/Suc_Edit.html'
    success_url = reverse_lazy('parametros:suc_panel')


class SucDelet(DeleteView):
    """Listado de Sucursales"""
    model = Sucursal
    form_class = SucursalForm
    template_name = 'parametros/Suc_Delet.html'
    success_url = reverse_lazy('parametros:suc_panel')

# ====================  Zipcodigo    =======================#


class ZipLista(ListView):
    """Listado de Zipcodigo"""
    model = Zipcodigo
    template_name = 'parametros/Zip_Panel.html'
    paginate_by = 8


class ZipView(DetailView):
    """Listado de Zipcodigo"""
    template_name = 'parametros/Zip_View.html'
    model = Zipcodigo


class ZipNuevo(CreateView):
    """Crear Zipcodigo"""
    model = Zipcodigo
    form_class = ZipcodigoForm
    template_name = 'parametros/Zip_New.html'
    success_url = reverse_lazy('parametros:zip_panel')


class ZipEdita(UpdateView):
    """Listado de Sucursales"""
    model = Zipcodigo
    form_class = ZipcodigoForm
    template_name = 'parametros/Zip_Edit.html'
    success_url = reverse_lazy('parametros:zip_panel')


class ZipDelet(DeleteView):
    """Listado de Sucursales"""
    model = Zipcodigo
    form_class = ZipcodigoForm
    template_name = 'parametros/Zip_Delet.html'
    success_url = reverse_lazy('parametros:zip_panel')

# ====================  Ciudad    =======================#


class CiuLista(ListView):
    """Listado de Ciudad"""
    model = Ciudad
    template_name = 'parametros/Ciu_Panel.html'
    paginate_by = 8


class CiuView(DetailView):
    """Listado de Ciudad"""
    template_name = 'parametros/Ciu_View.html'
    model = Ciudad
    form_class = CiudadForm


class CiuNuevo(CreateView):
    """Crear Ciudad"""
    model = Ciudad
    form_class = CiudadForm
    template_name = 'parametros/Ciu_New.html'
    success_url = reverse_lazy('parametros:ciu_panel')


class CiuEdita(UpdateView):
    """Listado de Ciudads"""
    model = Ciudad
    form_class = CiudadForm
    template_name = 'parametros/Ciu_Edit.html'
    success_url = reverse_lazy('parametros:ciu_panel')


class CiuDelet(DeleteView):
    """Listado de Ciudads"""
    model = Ciudad
    form_class = CiudadForm
    template_name = 'parametros/Ciu_Delet.html'
    success_url = reverse_lazy('parametros:ciu_panel')


# ====================  Provincia   =======================#


class PviLista(ListView):
    """Listado de Provincia"""
    model = Provincia
    template_name = 'parametros/Pvi_Panel.html'
    paginate_by = 8


class PviView(DetailView):
    """Listado de Provincia"""
    template_name = 'parametros/Pvi_View.html'
    model = Provincia


class PviNuevo(CreateView):
    """Crear Provincia"""
    model = Provincia
    form_class = ProvinciaForm
    template_name = 'parametros/Pvi_New.html'
    success_url = reverse_lazy('parametros:pvi_panel')


class PviEdita(UpdateView):
    """Listado de Provincias"""
    model = Provincia
    form_class = ProvinciaForm
    template_name = 'parametros/Pvi_Edit.html'
    success_url = reverse_lazy('parametros:pvi_panel')


class PviDelet(DeleteView):
    """Listado de Provincias"""
    model = Provincia
    form_class = ProvinciaForm
    template_name = 'parametros/Pvi_Delet.html'
    success_url = reverse_lazy('parametros:pvi_panel')

# ====================  Pais    =======================#


class PaiLista(ListView):
    """Listado de Pais"""
    model = Pais
    template_name = 'parametros/Pai_Panel.html'
    paginate_by = 8


class PaiView(DetailView):
    """Listado de Pais"""
    template_name = 'parametros/Pai_View.html'
    model = Pais


class PaiNuevo(CreateView):
    """Crear Pais"""
    model = Pais
    form_class = PaisForm
    template_name = 'parametros/Pai_New.html'
    success_url = reverse_lazy('parametros:pai_panel')


class PaiEdita(UpdateView):
    """Listado de Paiss"""
    model = Pais
    form_class = PaisForm
    template_name = 'parametros/Pai_Edit.html'
    success_url = reverse_lazy('parametros:pai_panel')


class PaiDelet(DeleteView):
    """Listado de Paiss"""
    model = Pais
    form_class = PaisForm
    template_name = 'parametros/Pai_Delet.html'
    success_url = reverse_lazy('parametros:pai_panel')
