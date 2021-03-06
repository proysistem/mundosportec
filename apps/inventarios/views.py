from __future__ import absolute_import, division, print_function, unicode_literals
import copy
from django.views.generic.base import TemplateResponseMixin, ContextMixin, View
from .rendering import render_to_pdf_response
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView
from django.db.models import Sum, Q
from .models import Division, Marca, Modelo, Color, Tabtalla, Existencia, Saldoxtalla
from .forms import (DivisionForm, MarcaForm, ModeloForm, ColorForm, TabtallaForm, ExistenciaForm,
                    SaldoxtallaForm, ExistenciaEditForm)
# from django.views.defaults import page_not_found
from django.http import Http404  # , HttpResponse
# import pdfkit
# from jinja2 import Environment, FileSystemLoader

# env = Environment(loader=FileSystemLoader("templates/inventarios/"))
# template = env.get_template("Exi_Pdf.html")
# from django_xhtml2pdf.views import PdfMixin

from django.contrib import messages

from multi_form_view import MultiModelFormView


# from django.views.generic import View
# from .utils import render_to_pdf  # created in step 4


# class ExiPrint(PdfMixin, DetailView):
#     model = Existencia
#     template_name = "inventarios/Exi_Pdf.html"


class ExiPdf(ListView):
    """docstring for ExiPdf"""
    model = Existencia
    template_name = 'inventarios/Exi_Pdf.html'
    ordering = ['exs_product']
    context_object_name = 'productos'
    # ordering = ['exs_product', 'exs_tabtall']
    # paginate_by = 54
    # queryset = Existencia.objects.filter(exs_saldact__gte=0.00)

    def get_queryset(self):
        return Existencia.objects.select_related('exs_idunida', 'saldoxtalla')

    def get_context_data(self, **kwargs):
        # html = super(ExiPdf, self).get_context_data(**kwargs)
        context = super(ExiPdf, self).get_context_data(**kwargs)
        context['totaldesaldos'] = self.get_queryset().aggregate(totaldesaldos=Sum('exs_saldact'))['totaldesaldos']
        # options = {
        #         'page-size': 'A5',
        #         'margin-top': '0.1in',
        #         'margin-right': '0.1in',
        #         'margin-bottom': '0.1in',
        #         'margin-left': '0.1in',
        # }
        # pdfkit.from_string(html, 'nuevo_pdf.pdf', options=options)
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


class PDFTemplateResponseMixin(TemplateResponseMixin):
    """
    A mixin class that implements PDF rendering and Django response construction.
    """

    #: Optional name of the PDF file for download. Leave blank for display in browser.
    pdf_filename = None

    #: Additional params passed to :func:`render_to_pdf_response`
    pdf_kwargs = None

    def get_pdf_filename(self):
        """
        Returns :attr:`pdf_filename` value by default.

        If left blank the browser will display the PDF inline.
        Otherwise it will pop up the "Save as.." dialog.

        :rtype: :func:`str`
        """
        return self.pdf_filename

    def get_pdf_kwargs(self):
        """
        Returns :attr:`pdf_kwargs` by default.

        The kwargs are passed to :func:`render_to_pdf_response` and
        :func:`xhtml2pdf.pisa.pisaDocument`.

        :rtype: :class:`dict`
        """
        if self.pdf_kwargs is None:
            return {}
        return copy.copy(self.pdf_kwargs)

    def get_pdf_response(self, context, **response_kwargs):
        """
        Renders PDF document and prepares response.

        :returns: Django HTTP response
        :rtype: :class:`django.http.HttpResponse`
        """
        return render_to_pdf_response(
            request=self.request,
            template=self.get_template_names('inventarios/Exi_Pdf.html'),
            context=context,
            using=self.template_engine,
            filename=self.get_pdf_filename(),
            **self.get_pdf_kwargs()
        )

    def render_to_response(self, context, **response_kwargs):
        return self.get_pdf_response(context, **response_kwargs)


class PDFTemplateView(PDFTemplateResponseMixin, ContextMixin, View):
    """
    Concrete view for serving PDF files.

    .. code-block:: python

        class HelloPDFView(PDFTemplateView):
            template_name = "hello.html"
    """

    def get(self, request, *args, **kwargs):
        """
        Handles GET request and returns HTTP response.
        """
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


# ====================================================================#
# ===============  D  I  V  I  S  I  O  N  E  S  =====================#
# ====================================================================#


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

# ====================================================================#
# ========================  M A R C A S ==============================#
# ====================================================================#


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

# ====================================================================#
# =====================  M O  D  E  L  O  S ==========================#
# ====================================================================#


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

# ====================================================================#
# ==================  C   O   L  O  R  E  S ==========================#
# ====================================================================#


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

# ====================================================================#
# ================  T  A  B  T  A  L  L  A  S  =======================#
# ====================================================================#


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

# ====================================================================#
# ==============  E  X  I  S  T  E  N  C  I  A  S  ===================#
# ====================================================================#


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
        # if self.request.GET.get('all', None) is None:
        #     queryset = queryset.filter(exs_saldact__gt=0.00)
        return queryset.filter(exs_sucursa=sucursal)


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


# class ExiEtiq(DetailView):
#     """Listado de Existencia"""
#     model = Existencia

#     def get_queryset(self):
#         contexto = Existencia.objects.select_related('saldoxtalla', 'exs_sucursa', 'exs_idmodel', 'exs_idmodel', 'exs_iddivis', 'exs_idmodel')
#         template = 'inventarios/Exi_Print.html'
#         html = template
#         pdf = render_to_pdf(template, contexto)
#         return HttpResponse(pdf, content_type='/inventarios/pdf')

# pdf = render_to_pdf('inventarios/Exi_Etiq.html', contexto)

#     def get_queryset(self):
#        return Existencia.objects.select_related('exs_idunida', 'saldoxtalla')
# class GeneratePdf(View):
#     def get(self, request, *args, **kwargs):
#         data = {
#             'today': datetime.date.today(),
#             'amount': 39.99,
#             'customer_name': 'Cooper Mann',
#             'order_id': 1233434,
#             }

# class GeneratePDF(View):
#     def get(self, request, *args, **kwargs):

#         template = get_template('invoice.html')
#         context = {
#             "invoice_id": 123,
#             "customer_name": "John Cooper",
#             "amount": 1399.99,
#             "today": "Today",
#         }
#         html = template.render(context)
#         pdf = render_to_pdf('invoice.html', context)

#         if pdf:
#             response = HttpResponse(pdf, content_type='application/pdf')
#             filename = "Invoice_%s.pdf" %("12341231")
#             content = "inline; filename='%s'" %(filename)
#             download = request.GET.get("download")
#             if download:
#                 content = "attachment; filename='%s'" %(filename)
#             response['Content-Disposition'] = content
#             return response
#         return HttpResponse("Not found")

def ReyTiket(request):
    n = 300
    context = {'tikets': range(11, n+1)}
    template = 'inventarios/Rey_Tiket.html'
    return render(request, template, context)


class ExiTiket(DetailView):
    """Listado de Existencia"""
    template_name = 'inventarios/Exi_Tiket.html'
    model = Existencia
    queryset = Existencia.objects.select_related('saldoxtalla', 'exs_sucursa', 'exs_idmodel', 'exs_idmodel', 'exs_iddivis', 'exs_idmodel')


class ExiTikts(ListView):
    """Reporte de Existencia"""
    model = Existencia
    template_name = 'inventarios/Exi_Tikts.html'
    ordering = ['exs_product']
    context_object_name = 'productos'

    def get_queryset(self):
        return Existencia.objects.select_related('exs_idunida', 'saldoxtalla')

    # def get_queryset(self):
        # queryset = super(ExiTiket, self).get_queryset()
        # user = self.request.user
        # sucursal = user.sucursal.pk
        # return queryset.filter(exs_sucursa=sucursal)

    # def get_context_data(self, **kwargs):
    #     context = super(ExiTiket, self).get_context_data(**kwargs)

    #     context['totaldesaldos'] = self.get_queryset().aggregate(totaldesaldos=Sum('exs_saldact'))['totaldesaldos']
    #     return context


class ExiLista(ListView):
    """Listado de Existencia"""
    model = Existencia
    template_name = 'inventarios/Exi_Panel.html'
    ordering = ['pk']
    paginate_by = 10

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
    """Pop de tallas para pedidos (VEENTAS) """
    template_name = 'comercial/Pop_Tallas.html'
    model = Existencia
    queryset = Existencia.objects.select_related('saldoxtalla', 'exs_sucursa', 'exs_idmodel', 'exs_idmodel', 'exs_iddivis', 'exs_idmodel')
    # TODO: VER CANT. QUERIES


class IngTalla(DetailView):
    """Pop de tallas para ingresos (COMPRAS)"""
    template_name = 'comercial/Ing_Tallas.html'
    model = Existencia
    queryset = Existencia.objects.select_related('saldoxtalla', 'exs_sucursa', 'exs_idmodel', 'exs_idmodel', 'exs_iddivis', 'exs_idmodel')
    # TODO: VER CANT. QUERIES


class ExiNuevo(CreateView):
    """Crear Existencia"""
    model = Existencia
    form_class = ExistenciaForm
    template_name = 'inventarios/Exi_New.html'

    def get_form_kwargs(self):
        kwargs = super(ExiNuevo, self).get_form_kwargs()
        try:
            user = self.request.user
        except:
            pass
        else:
            kwargs.update({"user": user})
        return kwargs

    def get_initial(self):
        initial = {}
        # import pdb; pdb.set_trace()
        try:
            sucursal = self.request.user.sucursal
        except:
            pass
        else:
            initial['exs_sucursa'] = sucursal.pk
        return initial

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

    def get_form_kwargs(self):
        kwargs = super(ExiEdita, self).get_form_kwargs()
        try:
            user = self.request.user
        except:
            pass
        else:
            kwargs.update({"user": user})
        return kwargs

    def get_initial(self):
        initial = {}
        try:
            sucursal = self.request.user.sucursal
        except:
            pass
        else:
            initial['exs_sucursa'] = sucursal.pk

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


class ExiBuscar(TemplateView):
    """Busqueda en Existencias"""
    def post(self, request, *args, **kwargs):
        # wrk_templt = self.get_template_names('comercial/Pop_Exis.html'),
        wrk_buscar = request.POST['fnd_myfound']
        wrk_itflag = request.POST['fnd_templat']
        if wrk_itflag == 'pop':
            wrk_template = 'comercial/Pop_Exis.html'
        elif wrk_itflag == 'panel':
            wrk_template = 'inventarios/Exi_Panel.html'
        else:
            # TODO: Mostrar error
            wrk_template = ''
            pass
        # import pdb; pdb.set_trace()
        # wrk_byprod = Existencia.objects.filter(exs_product=wrk_buscar)
        # TODO: Aumentar espectro de busqueda
        wrk_results = self.get_queryset().filter(
            Q(exs_product__contains=wrk_buscar) | Q(exs_detalle__icontains=wrk_buscar)
        )
        return render(request, wrk_template, {'productos': wrk_results, 'object_list': wrk_results, 'wrk_bydetal': True})
        # return render(request, 'comercial/Pop_Exis.html', {'productos': wrk_results, 'wrk_bydetal': True})

    def get_queryset(self):
        user = self.request.user
        sucursal = user.sucursal
        # return Existencia.objects.filter(exs_saldact__gt=0.00, exs_sucursa=sucursal)
        return Existencia.objects.filter(exs_sucursa=sucursal)

# ====================================================================#
# ==================  SALDOS  X  TALLAS  =============================#
# ====================================================================#


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
