# from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView
from django.db.models import Sum
from django.views.defaults import page_not_found
from django.http import Http404
from .models import Division, Marca, Modelo, Color, Tabtalla, Existencia, Saldoxtalla
from .forms import (DivisionForm, MarcaForm, ModeloForm, ColorForm, TabtallaForm, ExistenciaForm,
                    SaldoxtallaForm, ExistenciaEditForm)
# from apps.comercial.models import Cliente, Proveedor, Vendedor, Movinvent, Pedido, Factura
# {% extends 'base/base.html' %}

from django.contrib import messages

from multi_form_view import MultiModelFormView

# Create your views here.


class DivLista(ListView):
    """Listado de Division"""
    model = Division
    template_name = 'inventarios/Div_Panel.html'
    ordering = ['pk']
    paginate_by = 15


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


# class MrkSelect(ListView):
#   """Listado de Marca"""
#   model = Marca
#   template_name = 'inventarios/Prd_New.html'
#   context_object_name = 'slc_marcas'   ****--->> falta terminar para select-list dinamicas


class Mrkkyselect(ListView):
    model = Marca
    template_name = 'inventarios/Prd_Select.html'
    context_object_name = 'all_marcas'
#   paginate_by = 10

# ========M A R C A S=========== #


class MrkLista(ListView):
    """Listado de Marca"""
    model = Marca
    template_name = 'inventarios/Mrk_Panel.html'
    ordering = ['pk']
    paginate_by = 15


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
    ordering = ['pk']
    paginate_by = 15


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

    def form_invalid(self, form):
        messages.error(self.request, 'Hay un error en el formulario')
        return super(ModNuevo, self).form_invalid(form)


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
    ordering = ['pk']
    paginate_by = 15


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
    ordering = ['pk']
    paginate_by = 15


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


# ======== E  X  I  S  T  E  N  C  I  A  S =========== #

class PopExist(ListView):
    """Listado de Existencia"""
    model = Existencia
    template_name = 'comercial/Pop_Exis.html'
    ordering = ['pk']
    context_object_name = 'productos'
    paginate_by = 8

    def get_queryset(self):
        queryset = super(PopExist, self).get_queryset()
        user = self.request.user
        sucursal = user.sucursal
        return queryset.filter(exs_saldact__gt=0.00, exs_sucursa=sucursal)


class ExiQuery(DetailView):
    """Consulta de Existencia"""
    model = Existencia
    template_name = 'inventarios/Exi_Query.html'
    context_object_name = 'productos'

    slug_field = 'exs_product'
    slug_url_kwarg = 'exs_product'
    pk_url_kwarg = None

    def get(self, request, *args, **kwargs):
        contexto = {}
        try:
            self.object = self.get_object()
        except Http404:
            self.object = None
            contexto['err_err404'] = True
            contexto['probado'] = 'probando'
        context = self.get_context_data(object=self.object)
        context.update(contexto)
        return self.render_to_response(context)


class ExiPrint(ListView):
    """Reporte de Existencia"""
    model = Existencia
    template_name = 'inventarios/Exi_Print.html'
    ordering = ['exs_product']
    context_object_name = 'productos'
    # ordering = ['exs_product', 'exs_tabtall']
    # paginate_by = 54
    # queryset = Existencia.objects.filter(exs_saldact__gte=0.00)

    def get_queryset(self):
        return Existencia.objects.select_related('exs_idunida', 'saldoxtalla')

    def get_context_data(self, **kwargs):
        context = super(ExiPrint, self).get_context_data(**kwargs)
        context['totaldesaldos'] = self.get_queryset().aggregate(totaldesaldos=Sum('exs_saldact'))['totaldesaldos']
        return context

    def get_initial(self):
        tll_actual = {}
        try:
            sxt = Saldoxtalla.objects.get(tex_product=self.object)
        except:
            pass
        else:
            tll_actual['tex_actua01'] = sxt.tex_actua01
            tll_actual['tex_actua02'] = sxt.tex_actua02
            tll_actual['tex_actua03'] = sxt.tex_actua03
            tll_actual['tex_actua04'] = sxt.tex_actua04
            tll_actual['tex_actua05'] = sxt.tex_actua05
            tll_actual['tex_actua06'] = sxt.tex_actua06
            tll_actual['tex_actua07'] = sxt.tex_actua07
            tll_actual['tex_actua08'] = sxt.tex_actua08
            tll_actual['tex_actua09'] = sxt.tex_actua09
            tll_actual['tex_actua10'] = sxt.tex_actua10
            tll_actual['tex_actua11'] = sxt.tex_actua11
            tll_actual['tex_actua12'] = sxt.tex_actua12
            tll_actual['tex_actua13'] = sxt.tex_actua13
        return tll_actual


class ExiTiket(ListView):
    """Reporte de Existencia"""
    model = Existencia
    template_name = 'inventarios/Exi_Tiket.html'
    ordering = ['exs_product']
    context_object_name = 'productos'
    # ordering = ['exs_product', 'exs_tabtall']
    # paginate_by = 54
    # queryset = Existencia.objects.filter(exs_saldact__gte=0.00)

    def get_queryset(self):
        return Existencia.objects.select_related('exs_idunida', 'saldoxtalla')

    # def get_context_data(self, **kwargs):
    #     context = super(ExiTiket, self).get_context_data(**kwargs)

    #     context['totaldesaldos'] = self.get_queryset().aggregate(totaldesaldos=Sum('exs_saldact'))['totaldesaldos']
    #     return context

    # def get_initial(self):
    #     tll_actual = {}
    #     try:
    #         sxt = Saldoxtalla.objects.get(tex_product=self.object)
    #     except:
    #         pass
    #     else:
    #         tll_actual['tex_actua01'] = sxt.tex_actua01
    #         tll_actual['tex_actua02'] = sxt.tex_actua02
    #         tll_actual['tex_actua03'] = sxt.tex_actua03
    #         tll_actual['tex_actua04'] = sxt.tex_actua04
    #         tll_actual['tex_actua05'] = sxt.tex_actua05
    #         tll_actual['tex_actua06'] = sxt.tex_actua06
    #         tll_actual['tex_actua07'] = sxt.tex_actua07
    #         tll_actual['tex_actua08'] = sxt.tex_actua08
    #         tll_actual['tex_actua09'] = sxt.tex_actua09
    #         tll_actual['tex_actua10'] = sxt.tex_actua10
    #         tll_actual['tex_actua11'] = sxt.tex_actua11
    #         tll_actual['tex_actua12'] = sxt.tex_actua12
    #         tll_actual['tex_actua13'] = sxt.tex_actua13
    #     return tll_actual


class ExiLista(ListView):
    """Listado de Existencia"""
    model = Existencia
    template_name = 'inventarios/Exi_Panel.html'
    ordering = ['pk']
    paginate_by = 8

    def get_queryset(self):
        queryset = super(ExiLista, self).get_queryset()
        user = self.request.user
        sucursal = user.sucursal
        return queryset.filter(exs_sucursa=sucursal)


class ExiView(DetailView):
    """Listado de Existencia"""
    template_name = 'inventarios/Exi_View.html'
    model = Existencia
    queryset = Existencia.objects.select_related('saldoxtalla', 'exs_sucursa', 'exs_idmodel', 'exs_idmodel', 'exs_iddivis', 'exs_idmodel')
    # TODO: VER CANT. QUERIES
    # TODO: Evitar que el usuario ingrese a Detalle de Existencia que no sea de la misma sucursal



class PopTalla(DetailView):
    """Listado de Existencia"""
    template_name = 'comercial/Pop_Tallas.html'
    model = Existencia
    queryset = Existencia.objects.select_related('saldoxtalla', 'exs_sucursa', 'exs_idmodel', 'exs_idmodel', 'exs_iddivis', 'exs_idmodel')
    # TODO: VER CANT. QUERIES


class ExiNuevo(CreateView):
    """Crear Existencia"""
    model = Existencia
    form_class = ExistenciaForm
    template_name = 'inventarios/Exi_New.html'

    def get_success_url(self):
        return reverse_lazy('inventarios:exi_edit', kwargs={'pk': self.object.pk})


class TablaTalla(MultiModelFormView):
    """Generar Tabla de Tallas"""
    model = Saldoxtalla
    template_name = 'inventarios/tabla_talla.html'

    def get_initial(self):
        # import pdb; pdb.set_trace()
        # return {"tex_product": }
        return {}

    def get_context_data(self, **kwargs):
        context = super(TablaTalla, self).get_context_data(**kwargs)
        context["saldoxtalla_form"] = SaldoxtallaForm()
        # import pdb; pdb.set_trace()
        return context


class ExiEdita(UpdateView):
    """Listado de Existencias"""
    model = Existencia
    form_class = ExistenciaEditForm
    template_name = 'inventarios/Exi_Edit.html'
    success_url = reverse_lazy('inventarios:exi_panel')

    def get_initial(self):
        initial = {}
        try:
            sxt = Saldoxtalla.objects.get(tex_product=self.object)
        except:
            pass
        else:
            initial['tex_inici01'] = sxt.tex_inici01
            initial['tex_inici02'] = sxt.tex_inici02
            initial['tex_inici03'] = sxt.tex_inici03
            initial['tex_inici04'] = sxt.tex_inici04
            initial['tex_inici05'] = sxt.tex_inici05
            initial['tex_inici06'] = sxt.tex_inici06
            initial['tex_inici07'] = sxt.tex_inici07
            initial['tex_inici08'] = sxt.tex_inici08
            initial['tex_inici09'] = sxt.tex_inici09
            initial['tex_inici10'] = sxt.tex_inici10
            initial['tex_inici11'] = sxt.tex_inici11
            initial['tex_inici12'] = sxt.tex_inici12
            initial['tex_inici13'] = sxt.tex_inici13
            initial['tex_ingre01'] = sxt.tex_ingre01
            initial['tex_ingre02'] = sxt.tex_ingre02
            initial['tex_ingre03'] = sxt.tex_ingre03
            initial['tex_ingre04'] = sxt.tex_ingre04
            initial['tex_ingre05'] = sxt.tex_ingre05
            initial['tex_ingre06'] = sxt.tex_ingre06
            initial['tex_ingre07'] = sxt.tex_ingre07
            initial['tex_ingre08'] = sxt.tex_ingre08
            initial['tex_ingre09'] = sxt.tex_ingre09
            initial['tex_ingre10'] = sxt.tex_ingre10
            initial['tex_ingre11'] = sxt.tex_ingre11
            initial['tex_ingre12'] = sxt.tex_ingre12
            initial['tex_ingre13'] = sxt.tex_ingre13
            initial['tex_egres01'] = sxt.tex_egres01
            initial['tex_egres02'] = sxt.tex_egres02
            initial['tex_egres03'] = sxt.tex_egres03
            initial['tex_egres04'] = sxt.tex_egres04
            initial['tex_egres05'] = sxt.tex_egres05
            initial['tex_egres06'] = sxt.tex_egres06
            initial['tex_egres07'] = sxt.tex_egres07
            initial['tex_egres08'] = sxt.tex_egres08
            initial['tex_egres09'] = sxt.tex_egres09
            initial['tex_egres10'] = sxt.tex_egres10
            initial['tex_egres11'] = sxt.tex_egres11
            initial['tex_egres12'] = sxt.tex_egres12
            initial['tex_egres13'] = sxt.tex_egres13
            initial['tex_compr01'] = sxt.tex_compr01
            initial['tex_compr02'] = sxt.tex_compr02
            initial['tex_compr03'] = sxt.tex_compr03
            initial['tex_compr04'] = sxt.tex_compr04
            initial['tex_compr05'] = sxt.tex_compr05
            initial['tex_compr06'] = sxt.tex_compr06
            initial['tex_compr07'] = sxt.tex_compr07
            initial['tex_compr08'] = sxt.tex_compr08
            initial['tex_compr09'] = sxt.tex_compr09
            initial['tex_compr10'] = sxt.tex_compr10
            initial['tex_compr11'] = sxt.tex_compr11
            initial['tex_compr12'] = sxt.tex_compr12
            initial['tex_compr13'] = sxt.tex_compr13
        return initial


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
    paginate_by = 12


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
