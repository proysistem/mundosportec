# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView, TemplateView
from apps.comercial.models import Cliente, Proveedor, Vendedor, Movinvent, Pedido, Factura, Ingreso, Compra, Ajustecr, Notacred
from apps.comercial.forms import (ClienteForm, ProveedorForm, VendedorForm, MovinventInlineForm,
                                  MovinventForm, PedidoForm, FacturaForm, IngresoForm, CompraForm,
                                  AjustecrForm, NotacredForm)
from django.db import transaction
from django.db.models import F, Prefetch, Sum, Q
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect

from io import BytesIO
from datetime import date

from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table

# Create your views here.
# ======== C L I E N T E S =========== #


class CliLista(ListView):
    """Listado de Cliente"""
    model = Cliente
    template_name = 'comercial/Cli_Panel.html'
    paginate_by = 8


class CliView(DetailView):
    """Listado de Cliente"""
    template_name = 'comercial/Cli_View.html'
    model = Cliente


class CliNuevo(CreateView):
    """Crear Cliente"""
    model = Cliente
    form_class = ClienteForm
    template_name = 'comercial/Cli_New.html'
    success_url = reverse_lazy('comercial:cli_panel')


class CliEdita(UpdateView):
    """Listado de Clientes"""
    model = Cliente
    form_class = ClienteForm
    template_name = 'comercial/Cli_Edit.html'
    success_url = reverse_lazy('comercial:cli_panel')


class CliDelet(DeleteView):
    """Listado de Clientes"""
    model = Cliente
    form_class = ClienteForm
    template_name = 'comercial/Cli_Delet.html'
    success_url = reverse_lazy('comercial:cli_panel')

# ======== P R O V E E D O R E S =========== #


class PrvLista(ListView):
    """Listado de Proveedor"""
    model = Proveedor
    template_name = 'comercial/Prv_Panel.html'
    paginate_by = 8


class PrvView(DetailView):
    """Listado de Proveedor"""
    template_name = 'comercial/Prv_View.html'
    model = Proveedor


class PrvNuevo(CreateView):
    """Crear Proveedor"""
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'comercial/Prv_New.html'
    success_url = reverse_lazy('comercial:prv_panel')


class PrvEdita(UpdateView):
    """Listado de Proveedors"""
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'comercial/Prv_Edit.html'
    success_url = reverse_lazy('comercial:prv_panel')


class PrvDelet(DeleteView):
    """Listado de Proveedors"""
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'comercial/Prv_Delet.html'
    success_url = reverse_lazy('comercial:prv_panel')

# ======== V E N D E D O R E S =========== #


class VndLista(ListView):
    """Listado de Vendedor"""
    model = Vendedor
    template_name = 'comercial/Vnd_Panel.html'
    paginate_by = 8


class VndView(DetailView):
    """Listado de Vendedor"""
    template_name = 'comercial/Vnd_View.html'
    model = Vendedor


class VndNuevo(CreateView):
    """Crear Vendedor"""
    model = Vendedor
    form_class = VendedorForm
    template_name = 'comercial/Vnd_New.html'
    success_url = reverse_lazy('comercial:vnd_panel')


class VndEdita(UpdateView):
    """Listado de Vendedors"""
    model = Vendedor
    form_class = VendedorForm
    template_name = 'comercial/Vnd_Edit.html'
    success_url = reverse_lazy('comercial:vnd_panel')


class VndDelet(DeleteView):
    """Listado de Vendedors"""
    model = Vendedor
    form_class = VendedorForm
    template_name = 'comercial/Vnd_Delet.html'
    success_url = reverse_lazy('comercial:vnd_panel')


# ======== MOVIMIENTOS DE INVENTARIOS "MOVINVENT" =========== #


class MviBuscar(TemplateView):
    """Busqueda en Movimientos """
    paginate_by = 12

    def post(self, request, *args, **kwargs):
        wrk_buscar = request.POST['fnd_myfound']
        wrk_itflag = request.POST['fnd_templat']
        if wrk_itflag == 'movim':
            wrk_template = 'comercial/Mvi_Panel.html'
        elif wrk_itflag == 'panel':
            wrk_template = 'comercial/Mvi_Panel.html'
        else:
            # TODO: Mostrar error
            wrk_template = ''
        pass
        # import pdb; pdb.set_trace()
        # wrk_byprod = Movinvent.objects.filter(exs_product=wrk_buscar)
        # TODO: Aumentar espectro de busqueda
        wrk_results = self.get_queryset().filter(
            Q(mvi_nummovi=wrk_buscar) | Q(mvi_product__contains=wrk_buscar)
        )
        return render(request, wrk_template, {'movimiento': wrk_results, 'object_list': wrk_results, 'wrk_byprod': True})

    def get_queryset(self):
        return Movinvent.objects

    #     user = self.request.user
    #     sucursal = user.sucursal
    #     return Movinvent.objects.filter(exs_sucursa=sucursal)


class MviLista(ListView):
    """Listado de Movinvent"""
    model = Movinvent
    template_name = 'comercial/Mvi_Panel.html'
    paginate_by = 12


class MviView(DetailView):
    """Listado de Movinvent"""
    template_name = 'comercial/Mvi_View.html'
    model = Movinvent


class MviNuevo(CreateView):
    """Crear Movinvent"""
    model = Movinvent
    form_class = MovinventForm
    template_name = 'comercial/Mvi_New.html'
    success_url = reverse_lazy('comercial:mvi_panel')


class MviEdita(UpdateView):
    """Listado de Movinvents"""
    model = Movinvent
    form_class = MovinventForm
    template_name = 'comercial/Mvi_Edit.html'
    success_url = reverse_lazy('comercial:mvi_panel')


class MviDelet(DeleteView):
    """Listado de Movinvents"""
    model = Movinvent
    form_class = MovinventForm
    template_name = 'comercial/Mvi_Delet.html'
    success_url = reverse_lazy('comercial:mvi_panel')


# ======== I  N  G  R  E  S  O  S =========== #


class IngLista(ListView):
    """Listado de Ingresos"""
    model = Ingreso
    template_name = 'comercial/Ing_Panel.html'
    paginate_by = 8


class IngView(DetailView):
    """Visualiza Ingreso"""
    template_name = 'comercial/Ing_View.html'
    model = Ingreso


class IngNuevo(CreateView):
    """Crear Ingreso"""
    model = Ingreso
    form_class = IngresoForm
    template_name = 'comercial/Ing_New.html'

    def get_success_url(self):
        return reverse_lazy('comercial:ing_edit', kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(IngNuevo, self).get_context_data(**kwargs)

        if self.request.POST:
            # context['movimientos'] = MovinventFormset(self.request.POST, queryset=Movinvent.objects.select_related())
            context['nuevo_mov'] = MovinventInlineForm(self.request.POST)
        else:
            context['nuevo_mov'] = MovinventInlineForm()
            # TODO: Hay un problema de 0n queries, debido a la generación de múltiples formset con mismo queryset, probablemente
            #       Probé con select_related sin éxito aún.
        return context

    # TODO: Sobreescribir save y guardar datos de sucursal.
    # def post(self, request, *args, **kwargs):
    #     self.object = None
    #     form = self.get_form()
    #     import pdb; pdb.set_trace()
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

    def form_invalid(self, form):
        # import pdb; pdb.set_trace()
        return super(IngNuevo, self).form_invalid(form)

    def form_valid(self, form):
        context = self.get_context_data()
        nuevo_mov = context['nuevo_mov']
        # movimientos = context['movimientos']
        with transaction.atomic():
            self.object = form.save()

            if nuevo_mov.is_valid():
                mov_instance = nuevo_mov.save(commit=False)
                mov_instance.mvi_ningres = self.object
                mov_instance.mvi_fechmov = self.object.ing_feching
                mov_instance.mvi_proveed = self.object.ing_proveed
                mov_instance.mvi_vendedo = self.object.ing_vendedo
                mov_instance.mvi_tipomov = self.object.ing_tipomov
                mov_instance.save(commit=True)
            else:
                return self.form_invalid(form)
            # if movimientos.is_valid():
            #     # TODO: Validate per form in formset
            #     #       Although, formset.is_valid do this.
            #     # for form in movimientos:
            #     #     if form.is_valid():
            #     #         form.
            #     movimientos.instance = self.object
            #     movimientos.save()
        return super(IngNuevo, self).form_valid(form)


class IngEdita(UpdateView):
    """Modifica Ingresos"""
    model = Ingreso
    form_class = IngresoForm
    template_name = 'comercial/Ing_Edita.html'
    # formnam = 'comercial:ped_edit'

    def get_queryset(self):
        return Ingreso.objects.prefetch_related(Prefetch(
            'movinvent_set', queryset=Movinvent.objects.select_related('mvi_product').annotate(
                subtotal=F('mvi_kntidad') * F('mvi_precios'))))

    def get_success_url(self):
        return reverse_lazy('comercial:ing_edit', kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(IngEdita, self).get_context_data(**kwargs)

        if self.request.POST:
            # context['movimientos'] = MovinventFormset(self.request.POST, queryset=Movinvent.objects.select_related())
            context['nuevo_mov'] = MovinventInlineForm(self.request.POST)
        else:
            context['nuevo_mov'] = MovinventInlineForm()
            # TODO: Hay un problema de 0n queries, debido a la generación de múltiples formset con mismo queryset, probablemente
            #       Probé con select_related sin éxito aún.
            movimientos = self.object.movinvent_set.all()
            total = 0
            for movimiento in movimientos:
                total += movimiento.subtotal

            context['movimientos'] = movimientos
            context['total'] = total
        return context

    def form_invalid(self, form):
        return super(IngEdita, self).form_invalid(form)

    def form_valid(self, form):
        context = self.get_context_data()
        nuevo_mov = context['nuevo_mov']
        # movimientos = context['movimientos']
        with transaction.atomic():
            self.object = form.save()

            if nuevo_mov.is_valid():
                mov_instance = nuevo_mov.save(commit=False)
                mov_instance.mvi_ningres = self.object
                mov_instance.mvi_fechmov = self.object.ing_feching
                mov_instance.mvi_proveed = self.object.ing_proveed
                mov_instance.mvi_vendedo = self.object.ing_vendedo
                mov_instance.mvi_tipomov = self.object.ing_tipomov
                mov_instance.save(commit=True)
            else:
                return self.form_invalid(nuevo_mov)
            # if movimientos.is_valid():
            #     # TODO: Validate per form in formset
            #     #       Although, formset.is_valid do this.
            #     # for form in movimientos:
            #     #     if form.is_valid():
            #     #         form.
            #     movimientos.instance = self.object
            #     movimientos.save()
        return super(IngEdita, self).form_valid(form)


# ======== C O M P R A S =========== #

class ComLista(ListView):
    """Listado de Compra"""
    model = Compra
    template_name = 'comercial/Com_Panel.html'
    paginate_by = 12


class ComBuscar(TemplateView):
    """Busqueda en Compras """
    def post(self, request, *args, **kwargs):
        wrk_buscar = request.POST['fnd_myfound']
        wrk_itflag = request.POST['fnd_templat']
        if wrk_itflag == 'COMP':
            wrk_template = 'comercial/Com_Panel.html'
        elif wrk_itflag == 'panel':
            wrk_template = 'comercial/Com_Panel.html'
        else:
            # TODO: Mostrar error
            wrk_template = ''
        pass
        # import pdb; pdb.set_trace()
        # wrk_byprod = Movinvent.objects.filter(exs_product=wrk_buscar)
        # TODO: Aumentar espectro de busqueda
        wrk_results = self.get_queryset().filter(
            Q(com_facprov__icontains=wrk_buscar) | Q(com_proveed__prv_frsname__icontains=wrk_buscar)
        )
        return render(request, wrk_template, {'notascred': wrk_results, 'object_list': wrk_results, 'wrk_byproved': True})

    def get_queryset(self):
        return Compra.objects


class ComNuevo(CreateView):
    model = Compra
    form_class = CompraForm
    template_name = "comercial/Com_New.html"

    def get_context_data(self, **kwargs):
        context = super(ComNuevo, self).get_context_data(**kwargs)
        ingreso = getattr(self, 'ingreso', None)
        if ingreso:
            movimientos = self.ingreso.movinvent_set.select_related('mvi_product').annotate(
                subtotal=F('mvi_kntidad') * F('mvi_precios')).all()
            context['movimientos'] = movimientos

            suma_dsc = 0
            suma_iva = 0
            total = 0
            for movimiento in movimientos:
                total += movimiento.subtotal
                suma_dsc += movimiento.mvi_desctos
                suma_iva += (movimiento.subtotal - (movimiento.mvi_desctos)) * (movimiento.mvi_impuest/100)
            # context['movimientos'] = movimientos
            context['total'] = total
            context['suma_dsc'] = suma_dsc
            context['suma_iva'] = suma_iva
            context['total_iva'] = total + suma_iva - suma_dsc
        return context

    def get_success_url(self):
        # TODO: Ir a impresión de factura
        return reverse_lazy('comercial:ing_new')
        # , kwargs={"pk": self.object.pk}

    def post(self, request, *args, **kwargs):
        if 'sub_compra' in request.POST and 'ingreso_id' in request.POST:
            self.object = None
            request.POST = request.POST.copy()
            try:
                ingreso = Ingreso.objects.get(pk=request.POST['ingreso_id'])
            except Exception:
                pass
            else:
                # factura = Factura(
                #         fac_npedido=pedido,
                #         fac_cliente=pedido.ped_cliente,
                #         fac_vendedo=pedido.ped_vendedo,
                #         fac_fechfac=timezone.now()
                #     )
                # self.object = factura
                self.ingreso = ingreso
                form_data = {
                    'com_ningres': ingreso.ing_ningres,
                    'com_proveed': ingreso.ing_proveed.pk,
                    'com_vendedo': ingreso.ing_vendedo.pk,
                    'com_facprov': request.POST['facproveed'],
                    'com_fechcom': date.today()
                }

                request.POST.update(form_data)
                form = self.get_form()
                form.initial = form_data
                return self.form_invalid(form)
                # if form.is_valid():
                #     # pedido.ped_statreg = # TODO: Cambiar estado a Choices de Estado
                #     return self.form_valid(form)
                # else:
                #     return self.form_invalid(form)
        return super(ComNuevo, self).post(request, *args, **kwargs)


# ======== P E D I D O S =========== #


class PedLista(ListView):
    """Listado de Pedido"""
    model = Pedido
    template_name = 'comercial/Ped_Panel.html'
    paginate_by = 8


class PedView(DetailView):
    """Visualiza Pedido"""
    template_name = 'comercial/Ped_View.html'
    model = Pedido


class PedNuevo(CreateView):
    """Crear Pedido"""
    model = Pedido
    form_class = PedidoForm
    template_name = 'comercial/Ped_New.html'

    def get_success_url(self):
        return reverse_lazy('comercial:ped_edit', kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(PedNuevo, self).get_context_data(**kwargs)

        if self.request.POST:
            # context['movimientos'] = MovinventFormset(self.request.POST, queryset=Movinvent.objects.select_related())
            context['nuevo_mov'] = MovinventInlineForm(self.request.POST)
        else:
            context['nuevo_mov'] = MovinventInlineForm()
            # TODO: Hay un problema de 0n queries, debido a la generación de múltiples formset con mismo queryset, probablemente
            #       Probé con select_related sin éxito aún.
        return context

    # def post(self, request, *args, **kwargs):
    #     self.object = None
    #     form = self.get_form()
    #     import pdb; pdb.set_trace()
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

    def form_invalid(self, form):
        # import pdb; pdb.set_trace()
        return super(PedNuevo, self).form_invalid(form)

    def form_valid(self, form):
        context = self.get_context_data()
        nuevo_mov = context['nuevo_mov']
        # movimientos = context['movimientos']
        with transaction.atomic():
            self.object = form.save()

            if nuevo_mov.is_valid():
                mov_instance = nuevo_mov.save(commit=False)
                mov_instance.mvi_npedido = self.object
                mov_instance.mvi_fechmov = self.object.ped_fechped
                mov_instance.mvi_cliente = self.object.ped_cliente
                mov_instance.mvi_vendedo = self.object.ped_vendedo
                mov_instance.mvi_tipomov = self.object.ped_tipomov
                mov_instance.save(commit=True)
            else:
                return self.form_invalid(form)
            # if movimientos.is_valid():
            #     # TODO: Validate per form in formset
            #     #       Although, formset.is_valid do this.
            #     # for form in movimientos:
            #     #     if form.is_valid():
            #     #         form.
            #     movimientos.instance = self.object
            #     movimientos.save()
        return super(PedNuevo, self).form_valid(form)


class PedEdita(UpdateView):
    """Modifica Pedidos"""
    model = Pedido
    form_class = PedidoForm
    template_name = 'comercial/Ped_Edit.html'
    formnam = 'comercial:ped_edit'

    def get_queryset(self):
        return Pedido.objects.prefetch_related(Prefetch(
            'movinvent_set', queryset=Movinvent.objects.select_related('mvi_product').annotate(
                subtotal=F('mvi_kntidad') * F('mvi_precios'))))

    def get_success_url(self):
        return reverse_lazy('comercial:ped_edit', kwargs={"pk": self.object.pk})

    # def get_success_url(self):
    #     if request.method == 'POST' and 'sub_factura' in self.request.POST:
    #         return reverse_lazy('comercial:fac_edit', kwargs={"pk": self.object.pk})
    #     else:
    #         return reverse_lazy('comercial:ped_edit', kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(PedEdita, self).get_context_data(**kwargs)

        if self.request.POST:
            # context['movimientos'] = MovinventFormset(self.request.POST, queryset=Movinvent.objects.select_related())
            context['nuevo_mov'] = MovinventInlineForm(self.request.POST)
        else:
            context['nuevo_mov'] = MovinventInlineForm()
            # TODO: Hay un problema de 0n queries, debido a la generación de múltiples formset con mismo queryset, probablemente
            #       Probé con select_related sin éxito aún.
            movimientos = self.object.movinvent_set.all()
            total = 0
            for movimiento in movimientos:
                total += movimiento.subtotal

            context['movimientos'] = movimientos
            context['total'] = total
        return context

    def form_invalid(self, form):
        return super(PedEdita, self).form_invalid(form)

    def form_valid(self, form):
        context = self.get_context_data()
        nuevo_mov = context['nuevo_mov']
        # movimientos = context['movimientos']
        with transaction.atomic():
            self.object = form.save()

            if nuevo_mov.is_valid():
                mov_instance = nuevo_mov.save(commit=False)
                mov_instance.mvi_npedido = self.object
                mov_instance.mvi_fechmov = self.object.ped_fechped
                mov_instance.mvi_cliente = self.object.ped_cliente
                mov_instance.mvi_vendedo = self.object.ped_vendedo
                mov_instance.mvi_tipomov = self.object.ped_tipomov
                mov_instance.save(commit=True)
            else:
                return self.form_invalid(nuevo_mov)
            # if movimientos.is_valid():
            #     # TODO: Validate per form in formset
            #     #       Although, formset.is_valid do this.
            #     # for form in movimientos:
            #     #     if form.is_valid():
            #     #         form.
            #     movimientos.instance = self.object
            #     movimientos.save()
        return super(PedEdita, self).form_valid(form)

    # def get_initial(self):
    #     initial = {}
    #     try:
    #         sxt = Saldoxtalla.objects.get(tex_product=self.object)
    #     except:
    #         pass
    #     else:
    #         initial['tex_inici01'] = sxt.tex_inici01
    #         initial['tex_inici02'] = sxt.tex_inici02
    #         initial['tex_inici03'] = sxt.tex_inici03
    #         initial['tex_inici04'] = sxt.tex_inici04
    #         initial['tex_inici05'] = sxt.tex_inici05
    #         initial['tex_inici06'] = sxt.tex_inici06
    #         initial['tex_inici07'] = sxt.tex_inici07
    #         initial['tex_inici08'] = sxt.tex_inici08
    #         initial['tex_inici09'] = sxt.tex_inici09
    #         initial['tex_inici10'] = sxt.tex_inici10
    #         initial['tex_inici11'] = sxt.tex_inici11
    #         initial['tex_inici12'] = sxt.tex_inici12
    #         initial['tex_inici13'] = sxt.tex_inici13
    #         initial['tex_ingre01'] = sxt.tex_ingre01
    #         initial['tex_ingre02'] = sxt.tex_ingre02
    #         initial['tex_ingre03'] = sxt.tex_ingre03
    #         initial['tex_ingre04'] = sxt.tex_ingre04
    #         initial['tex_ingre05'] = sxt.tex_ingre05
    #         initial['tex_ingre06'] = sxt.tex_ingre06
    #         initial['tex_ingre07'] = sxt.tex_ingre07
    #         initial['tex_ingre08'] = sxt.tex_ingre08
    #         initial['tex_ingre09'] = sxt.tex_ingre09
    #         initial['tex_ingre10'] = sxt.tex_ingre10
    #         initial['tex_ingre11'] = sxt.tex_ingre11
    #         initial['tex_ingre12'] = sxt.tex_ingre12
    #         initial['tex_ingre13'] = sxt.tex_ingre13
    #         initial['tex_egres01'] = sxt.tex_egres01
    #         initial['tex_egres02'] = sxt.tex_egres02
    #         initial['tex_egres03'] = sxt.tex_egres03
    #         initial['tex_egres04'] = sxt.tex_egres04
    #         initial['tex_egres05'] = sxt.tex_egres05
    #         initial['tex_egres06'] = sxt.tex_egres06
    #         initial['tex_egres07'] = sxt.tex_egres07
    #         initial['tex_egres08'] = sxt.tex_egres08
    #         initial['tex_egres09'] = sxt.tex_egres09
    #         initial['tex_egres10'] = sxt.tex_egres10
    #         initial['tex_egres11'] = sxt.tex_egres11
    #         initial['tex_egres12'] = sxt.tex_egres12
    #         initial['tex_egres13'] = sxt.tex_egres13
    #         initial['tex_compr01'] = sxt.tex_compr01
    #         initial['tex_compr02'] = sxt.tex_compr02
    #         initial['tex_compr03'] = sxt.tex_compr03
    #         initial['tex_compr04'] = sxt.tex_compr04
    #         initial['tex_compr05'] = sxt.tex_compr05
    #         initial['tex_compr06'] = sxt.tex_compr06
    #         initial['tex_compr07'] = sxt.tex_compr07
    #         initial['tex_compr08'] = sxt.tex_compr08
    #         initial['tex_compr09'] = sxt.tex_compr09
    #         initial['tex_compr10'] = sxt.tex_compr10
    #         initial['tex_compr11'] = sxt.tex_compr11
    #         initial['tex_compr12'] = sxt.tex_compr12
    #         initial['tex_compr13'] = sxt.tex_compr13
    #     return initial


# https://www.pythoniza.me/pdfs-en-django-con-reportlab/
class PedRepor(ListView):
    model = Pedido
    template_name = "comercial/Ped_Report.html"
    # context_object_name = "c"


def generar_pdf(request):
    ''' print "Genero el PDF" '''
    response = HttpResponse(content_type='application/pdf')
    # las 2 lineas siguientes son por si deseas descargar el pdf a tu computadora
    # pdf_name = "pedidos.pdf"                                      # llamado "pedidos.pdf"
    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()                                                # almacenamos BytesIO a la variable buff
    doc = SimpleDocTemplate(buff,                                   # configuramos nuestro documento
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    pedido = []                                                     # creamos una lista
    styles = getSampleStyleSheet()                                  # almacenamos getSampleStyleSheet a una variable llamada styles
    header = Paragraph("Listado de pedidos", styles['Heading1'])    # agregamos un titulo a nuestro documento usando Paragraph
    pedido.append(header)
    headings = ('Nombre', 'Email', 'Edad', 'Dirección')             # agregamos los encabezaos de las Columnas
    #                                                               # aqui creamos una variable que almacena todos los datos que tengo en el modelo Clientes
    allpedidos = [(p.nombre, p.email, p.edad, p.direccion) for p in pedido.objects.all()]
    print(allpedidos)

    #                                                               # creo una variable donde agrego a Table los nombres de las columnas con sus datos
    #                                                               # correspondientes que están el allclientes
    t = Table([headings] + allpedidos)
    t.setStyle(TableStyle(                                          # doy color a la tabla
        [
            ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))
    pedido.append(t)                                                # agrego todo a mi lista
    doc.build(pedido)                                               # genero el documento a partir de la lista clientes
    response.write(buff.getvalue())                                 # Recupero el archivo almacenado
    buff.close()                                                    # Librero la memoria
    return response                                                 # regreso la respuesta


class PedDelet(DeleteView):
    """Elimina  Pedidos"""
    model = Pedido
    form_class = PedidoForm
    template_name = 'comercial/Ped_Delet.html'
    success_url = reverse_lazy('comercial:ped_panel')

# ======== F A C T U R A S =========== #


class FacBuscar(TemplateView):
    """Busqueda en Factura """
    paginate_by = 10

    def post(self, request, *args, **kwargs):
        wrk_buscar = request.POST['fnd_myfound']
        wrk_itflag = request.POST['fnd_templat']
        if wrk_itflag == 'FACT':
            wrk_template = 'comercial/Fac_Panel.html'
        elif wrk_itflag == 'panel':
            wrk_template = 'comercial/Fac_Panel.html'
        else:
            # TODO: Mostrar error
            wrk_template = ''
        pass
        # import pdb; pdb.set_trace()
        # wrk_byprod = Movinvent.objects.filter(exs_product=wrk_buscar)
        # TODO: Aumentar espectro de busqueda
        wrk_results = self.get_queryset().filter(
            Q(fac_ctrlfac__icontains=wrk_buscar) |
            Q(fac_cliente__clt_frsname__icontains=wrk_buscar) |
            Q(fac_cliente__clt_midname__icontains=wrk_buscar) |
            Q(fac_cliente__clt_secmane__icontains=wrk_buscar))
        return render(request, wrk_template, {'facturas': wrk_results, 'object_list': wrk_results, 'wrk_bycliente': True})

    def get_queryset(self):
        return Factura.objects

    #     user = self.request.user
    #     sucursal = user.sucursal
    #     return Movinvent.objects.filter(exs_sucursa=sucursal)


class FacLista(ListView):
    """Listado de Facturas"""
    model = Factura
    template_name = 'comercial/Fac_Panel.html'
    paginate_by = 10


class FacPrint(ListView):
    """Listado de Facturas"""
    model = Factura
    template_name = 'comercial/Ped_New.html'
    paginate_by = 8


class FacView(DetailView):
    """Visualiza reg. Factura"""
    template_name = 'comercial/Fac_View.html'
    model = Factura


class FacNuevo(CreateView):
    """Crear Cliente"""
    model = Factura
    form_class = FacturaForm
    template_name = 'comercial/Fac_New.html'
    # success_url = reverse_lazy('comercial:fac_panel')

    def form_valid(self, form):
        # import pdb; pdb.set_trace()
        self.object = form.save(request=self.request)
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(FacNuevo, self).get_context_data(**kwargs)
        pedido = getattr(self, 'pedido', None)
        if pedido:
            movimientos = self.pedido.movinvent_set.select_related('mvi_product').annotate(
                subtotal=F('mvi_kntidad') * F('mvi_precios')).all()
            context['movimientos'] = movimientos

            suma_dsc = 0
            suma_iva = 0
            total = 0
            for movimiento in movimientos:
                total += movimiento.subtotal
                suma_dsc += movimiento.mvi_desctos
                suma_iva += (movimiento.subtotal - (movimiento.mvi_desctos)) * (movimiento.mvi_impuest/100)
            # context['movimientos'] = movimientos
            context['total'] = total
            context['suma_dsc'] = suma_dsc
            context['suma_iva'] = suma_iva
            context['total_iva'] = total + suma_iva - suma_dsc
        return context

    def get_success_url(self):
        # TODO: Ir a impresión de factura
        return reverse_lazy('comercial:ped_new')
        # , kwargs={"pk": self.object.pk}

    def post(self, request, *args, **kwargs):
        if 'sub_factura' in request.POST and 'pedido_id' in request.POST:
            self.object = None
            request.POST = request.POST.copy()
            try:
                pedido = Pedido.objects.get(pk=request.POST['pedido_id'])
            except Exception:
                pass
            else:
                # factura = Factura(
                #         fac_npedido=pedido,
                #         fac_cliente=pedido.ped_cliente,
                #         fac_vendedo=pedido.ped_vendedo,
                #         fac_fechfac=timezone.now()
                #     )
                # self.object = factura
                self.pedido = pedido
                form_data = {
                    'fac_npedido': pedido.ped_npedido,
                    'fac_cliente': pedido.ped_cliente.pk,
                    'fac_vendedo': pedido.ped_vendedo.pk,
                    'fac_fechfac': timezone.now()
                }
                request.POST.update(form_data)
                form = self.get_form()
                form.initial = form_data
                return self.form_invalid(form)
                # if form.is_valid():
                #     # pedido.ped_statreg = # TODO: Cambiar estado a Choices de Estado
                #     return self.form_valid(form)
                # else:
                #     return self.form_invalid(form)
        return super(FacNuevo, self).post(request, *args, **kwargs)


class FacEdita(UpdateView):
    """Actualiza Factura"""
    model = Factura
    form_class = FacturaForm
    template_name = 'comercial/Fac_Edit.html'
    success_url = reverse_lazy('comercial:ped_new')

    def get_queryset(self):
        return Factura.objects.prefetch_related(Prefetch(
            'fac_npedido__movinvent_set', queryset=Movinvent.objects.select_related('mvi_product').annotate(
                subtotal=F('mvi_kntidad') * F('mvi_precios'))))

    def get_context_data(self, **kwargs):
        context = super(FacEdita, self).get_context_data(**kwargs)
        total = 0
        movimientos = self.get_object().fac_npedido.movinvent_set.all()
        for movimiento in movimientos:
            total += movimiento.subtotal
        # context['movimientos'] = movimientos
        context['total'] = total
        return context


class FacDelet(DeleteView):
    """Elimina Factura"""
    model = Factura
    form_class = FacturaForm
    template_name = 'comercial/Fac_Delet.html'
    success_url = reverse_lazy('comercial:fac_panel')


class FacPaid(UpdateView):
    """Crea factura"""
    model = Pedido
    form_class = PedidoForm
    template_name = 'comercial/Fac_Edit.html'

    def get_queryset(self):
        return Pedido.objects.prefetch_related(Prefetch(
            'movinvent_set', queryset=Movinvent.objects.select_related('mvi_product').annotate(
                subtotal=F('mvi_kntidad') * F('mvi_precios'))))

    def get_success_url(self):
        return reverse_lazy('comercial:fac_edit', kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(PedEdita, self).get_context_data(**kwargs)

        if self.request.POST:
            # context['movimientos'] = MovinventFormset(self.request.POST, queryset=Movinvent.objects.select_related())
            context['nuevo_mov'] = MovinventInlineForm(self.request.POST)
        else:
            context['nuevo_mov'] = MovinventInlineForm()
            # TODO: Hay un problema de 0n queries, debido a la generación de múltiples formset con mismo queryset, probablemente
            #       Probé con select_related sin éxito aún.
            movimientos = self.object.movinvent_set.all()
            total = 0
            for movimiento in movimientos:
                total += movimiento.subtotal

            context['movimientos'] = movimientos
            context['total'] = total
        return context

    # def form_invalid(self, form):
    #     return super(PedEdita, self).form_invalid(form)

    def form_valid(self, form):
        context = self.get_context_data()
        nuevo_mov = context['nuevo_mov']
        # movimientos = context['movimientos']
        with transaction.atomic():
            self.object = form.save()

            if nuevo_mov.is_valid():
                mov_instance = nuevo_mov.save(commit=False)
                mov_instance.mvi_npedido = self.object
                mov_instance.mvi_fechmov = self.object.ped_fechped
                mov_instance.mvi_cliente = self.object.ped_cliente
                mov_instance.mvi_vendedo = self.object.ped_vendedo
                mov_instance.mvi_tipomov = self.object.ped_tipomov
                mov_instance.save(commit=True)
            else:
                return self.form_invalid(nuevo_mov)
            # if movimientos.is_valid():
            #     # TODO: Validate per form in formset
            #     #       Although, formset.is_valid do this.
            #     # for form in movimientos:
            #     #     if form.is_valid():
            #     #         form.
            #     movimientos.instance = self.object
            #     movimientos.save()
        return super(PedEdita, self).form_valid(form)

# ========    =========== #


# ======== A J U S T E  POR  C R E D I T O S =========== #


class AjcLista(ListView):
    """Listado de Ajustecr"""
    model = Ajustecr
    template_name = 'comercial/Ajc_Panel.html'
    paginate_by = 12


class AjcView(DetailView):
    """Visualiza Ajustecr"""
    template_name = 'comercial/Ajc_View.html'
    model = Ajustecr


class AjcNuevo(CreateView):
    """Crear Ajustecr"""
    model = Ajustecr
    form_class = AjustecrForm
    template_name = 'comercial/Ajc_New.html'

    def get_success_url(self):
        return reverse_lazy('comercial:ajc_edit', kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(AjcNuevo, self).get_context_data(**kwargs)

        if self.request.POST:
            # context['movimientos'] = MovinventFormset(self.request.POST, queryset=Movinvent.objects.select_related())
            context['nuevo_mov'] = MovinventInlineForm(self.request.POST)
        else:
            context['nuevo_mov'] = MovinventInlineForm()
            # TODO: Hay un problema de 0n queries, debido a la generación de múltiples formset con mismo queryset, probablemente
            #       Probé con select_related sin éxito aún.
        return context

    # def post(self, request, *args, **kwargs):
    #     self.object = None
    #     form = self.get_form()
    #     import pdb; pdb.set_trace()
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

    def form_invalid(self, form):
        # import pdb; pdb.set_trace()
        return super(AjcNuevo, self).form_invalid(form)

    def form_valid(self, form):
        context = self.get_context_data()
        nuevo_mov = context['nuevo_mov']
        # movimientos = context['movimientos']
        with transaction.atomic():
            self.object = form.save()

            if nuevo_mov.is_valid():
                mov_instance = nuevo_mov.save(commit=False)
                mov_instance.mvi_najustc = self.object
                mov_instance.mvi_fechmov = self.object.ajc_fechajs
                mov_instance.mvi_cliente = self.object.ajc_cliente
                mov_instance.mvi_vendedo = self.object.ajc_vendedo
                mov_instance.mvi_tipomov = self.object.ajc_tipomov
                mov_instance.save(commit=True)
            else:
                return self.form_invalid(form)
            # if movimientos.is_valid():
            #     # TODO: Validate per form in formset
            #     #       Although, formset.is_valid do this.
            #     # for form in movimientos:
            #     #     if form.is_valid():
            #     #         form.
            #     movimientos.instance = self.object
            #     movimientos.save()
        return super(AjcNuevo, self).form_valid(form)


class AjcEdita(UpdateView):
    """Modifica Ajustecr"""
    model = Ajustecr
    form_class = AjustecrForm
    template_name = 'comercial/Ajc_Edit.html'
    formnam = 'comercial:ajc_edit'

    def get_queryset(self):
        return Ajustecr.objects.prefetch_related(Prefetch(
            'movinvent_set', queryset=Movinvent.objects.select_related('mvi_product').annotate(
                subtotal=F('mvi_kntidad') * F('mvi_precios'))))

    def get_success_url(self):
        return reverse_lazy('comercial:ajc_edit', kwargs={"pk": self.object.pk})

    # def get_success_url(self):
    #     if request.method == 'POST' and 'sub_factura' in self.request.POST:
    #         return reverse_lazy('comercial:fac_edit', kwargs={"pk": self.object.pk})
    #     else:
    #         return reverse_lazy('comercial:ajc_edit', kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(AjcEdita, self).get_context_data(**kwargs)

        if self.request.POST:
            # context['movimientos'] = MovinventFormset(self.request.POST, queryset=Movinvent.objects.select_related())
            context['nuevo_mov'] = MovinventInlineForm(self.request.POST)
        else:
            context['nuevo_mov'] = MovinventInlineForm()
            # TODO: Hay un problema de 0n queries, debido a la generación de múltiples formset con mismo queryset, probablemente
            #       Probé con select_related sin éxito aún.
            movimientos = self.object.movinvent_set.all()
            total = 0
            for movimiento in movimientos:
                total += movimiento.subtotal

            context['movimientos'] = movimientos
            context['total'] = total
        return context

    def form_invalid(self, form):
        return super(AjcEdita, self).form_invalid(form)

    def form_valid(self, form):
        context = self.get_context_data()
        nuevo_mov = context['nuevo_mov']
        # movimientos = context['movimientos']
        with transaction.atomic():
            self.object = form.save()

            if nuevo_mov.is_valid():
                mov_instance = nuevo_mov.save(commit=False)
                mov_instance.mvi_najustc = self.object
                mov_instance.mvi_fechmov = self.object.ajc_fechajs
                mov_instance.mvi_cliente = self.object.ajc_cliente
                mov_instance.mvi_vendedo = self.object.ajc_vendedo
                mov_instance.mvi_tipomov = self.object.ajc_tipomov
                mov_instance.save(commit=True)
            else:
                return self.form_invalid(nuevo_mov)
            # if movimientos.is_valid():
            #     # TODO: Validate per form in formset
            #     #       Although, formset.is_valid do this.
            #     # for form in movimientos:
            #     #     if form.is_valid():
            #     #         form.
            #     movimientos.instance = self.object
            #     movimientos.save()
        return super(AjcEdita, self).form_valid(form)


# https://www.pythoniza.me/pdfs-en-django-con-reportlab/
class AjcRepor(ListView):
    model = Ajustecr
    template_name = "comercial/Ajc_Report.html"
    # context_object_name = "c"


class AjcDelet(DeleteView):
    """Elimina  Ajustecrs"""
    model = Ajustecr
    form_class = AjustecrForm
    template_name = 'comercial/Ajc_Delet.html'
    success_url = reverse_lazy('comercial:ajc_panel')

# ======== N O T A   DE   C R E D I T O =========== #


class NcrBuscar(TemplateView):
    """Busqueda en Notacred """
    paginate_by = 10

    def post(self, request, *args, **kwargs):
        wrk_buscar = request.POST['fnd_myfound']
        wrk_itflag = request.POST['fnd_templat']
        if wrk_itflag == 'NOTA':
            wrk_template = 'comercial/Ncr_Panel.html'
        elif wrk_itflag == 'panel':
            wrk_template = 'comercial/Ncr_Panel.html'
        else:
            # TODO: Mostrar error
            wrk_template = ''
        pass
        # import pdb; pdb.set_trace()
        # wrk_byprod = Movinvent.objects.filter(exs_product=wrk_buscar)
        # TODO: Aumentar espectro de busqueda
        wrk_results = self.get_queryset().filter(
            Q(ncr_ctrlnta__icontains=wrk_buscar) |
            Q(ncr_cliente__clt_frsname__icontains=wrk_buscar) |
            Q(ncr_cliente__clt_midname__icontains=wrk_buscar) |
            Q(ncr_cliente__clt_secmane__icontains=wrk_buscar))
        return render(request, wrk_template, {'notacred': wrk_results, 'object_list': wrk_results, 'wrk_bycliente': True})

    def get_queryset(self):
        return Notacred.objects

    #     user = self.request.user
    #     sucursal = user.sucursal
    #     return Movinvent.objects.filter(exs_sucursa=sucursal)


class NcrLista(ListView):
    """Listado de Notacred"""
    model = Notacred
    template_name = 'comercial/Ncr_Panel.html'
    paginate_by = 12


class NcrPrint(ListView):
    """Listado de Notacred"""
    model = Notacred
    template_name = 'comercial/Ncr_New.html'
    paginate_by = 12


class NcrView(DetailView):
    """Visualiza reg. Notacred"""
    template_name = 'comercial/Ncr_View.html'
    model = Notacred


class NcrNuevo(CreateView):
    """Crear Notacred"""
    model = Notacred
    form_class = NotacredForm
    template_name = 'comercial/Ncr_New.html'
    # success_url = reverse_lazy('comercial:ncr_panel')

    def form_valid(self, form):
        # import pdb,  pdb.set_trace()
        self.object = form.save(request=self.request)
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(NcrNuevo, self).get_context_data(**kwargs)
        ajustecr = getattr(self, 'ajustecr', None)
        if ajustecr:
            movimientos = self.ajustecr.movinvent_set.select_related('mvi_product').annotate(
                subtotal=F('mvi_kntidad') * F('mvi_precios')).all()
            context['movimientos'] = movimientos

            suma_dsc = 0
            suma_iva = 0
            total = 0
            for movimiento in movimientos:
                total += movimiento.subtotal
                suma_dsc += movimiento.mvi_desctos
                suma_iva += (movimiento.subtotal - (movimiento.mvi_desctos)) * (movimiento.mvi_impuest/100)
            # context['movimientos'] = movimientos
            context['total'] = total
            context['suma_dsc'] = suma_dsc
            context['suma_iva'] = suma_iva
            context['total_iva'] = total + suma_iva - suma_dsc
        return context

    def get_success_url(self):
        # TODO: Ir a impresión de factura
        return reverse_lazy('comercial:ajc_new')
        # , kwargs={"pk": self.object.pk}

    def post(self, request, *args, **kwargs):
        if 'sub_notacred' in request.POST and 'ajustecr_id' in request.POST:
            self.object = None
            request.POST = request.POST.copy()
            try:
                ajustecr = Ajustecr.objects.get(pk=request.POST['ajustecr_id'])
            except Exception:
                pass
            else:
                # factura = Factura(
                #         fac_npedido=ajustecr,
                #         fac_cliente=ajustecr.ped_cliente,
                #         fac_vendedo=ajustecr.ped_vendedo,
                #         fac_fechfac=timezone.now()
                #     )
                # self.object = factura
                self.ajustecr = ajustecr
                form_data = {
                    'ncr_najuste': ajustecr.ajc_najustc,
                    'ncr_cliente': ajustecr.ajc_cliente.pk,
                    'ncr_vendedo': ajustecr.ajc_vendedo.pk,
                    'ncr_fechnta': timezone.now(),
                }
                request.POST.update(form_data)
                form = self.get_form()
                form.initial = form_data
                return self.form_invalid(form)
                # if form.is_valid():
                #     # ajustecr.ped_statreg = # TODO: Cambiar estado a Choices de Estado
                #     return self.form_valid(form)
                # else:
                #     return self.form_invalid(form)
        return super(NcrNuevo, self).post(request, *args, **kwargs)


class NcrEdita(UpdateView):
    """Actualiza Notacred"""
    model = Notacred
    form_class = NotacredForm
    template_name = 'comercial/Ncr_Edit.html'
    success_url = reverse_lazy('comercial:ajc_new')

    def get_queryset(self):
        return Notacred.objects.prefetch_related(Prefetch(
            'ncr_najuste__movinvent_set', queryset=Movinvent.objects.select_related('mvi_product').annotate(
                subtotal=F('mvi_kntidad') * F('mvi_precios'))))

    def get_context_data(self, **kwargs):
        context = super(NcrEdita, self).get_context_data(**kwargs)
        total = 0
        movimientos = self.get_object().ncr_najuste.movinvent_set.all()
        for movimiento in movimientos:
            total += movimiento.subtotal
        # context['movimientos'] = movimientos
        context['total'] = total
        return context


class NcrDelet(DeleteView):
    """Elimina Notacred"""
    model = Notacred
    form_class = NotacredForm
    template_name = 'comercial/Ncr_Delet.html'
    success_url = reverse_lazy('comercial:ncr_panel')
