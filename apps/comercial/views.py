from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from apps.comercial.models import Cliente, Proveedor, Vendedor, Movinvent, Pedido, Factura
from apps.comercial.forms import ClienteForm, ProveedorForm, VendedorForm, MovinventForm, PedidoForm, FacturaForm
from django.db import transaction
from django.forms import inlineformset_factory

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

class MviLista(ListView):
    """Listado de Movinvent"""
    model = Movinvent
    template_name = 'conercial/Mvi_Panel.html'
    paginate_by = 8


class MviView(DetailView):
    """Listado de Movinvent"""
    template_name = 'conercial/Mvi_View.html'
    model = Movinvent


class MviNuevo(CreateView):
    """Crear Movinvent"""
    model = Movinvent
    form_class = MovinventForm
    template_name = 'conercial/Mvi_New.html'
    success_url = reverse_lazy('comercial:mvi_panel')


class MviEdita(UpdateView):
    """Listado de Movinvents"""
    model = Movinvent
    form_class = MovinventForm
    template_name = 'conercial/Mvi_Edit.html'
    success_url = reverse_lazy('comercial:mvi_panel')


class MviDelet(DeleteView):
    """Listado de Movinvents"""
    model = Movinvent
    form_class = MovinventForm
    template_name = 'conercial/Mvi_Delet.html'
    success_url = reverse_lazy('comercial:mvi_panel')

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
    success_url = reverse_lazy('comercial:ped_panel')


class PedEdita(UpdateView):
    """Modifica Pedidos"""
    model = Pedido
    form_class = PedidoForm
    template_name = 'comercial/Ped_Edit.html'
    success_url = reverse_lazy('comercial:ped_panel')


class PedDelet(DeleteView):
    """Elimina  Pedidos"""
    model = Pedido
    form_class = PedidoForm
    template_name = 'comercial/Ped_Delet.html'
    success_url = reverse_lazy('comercial:ped_panel')

# ======== F A C T U R A S =========== #


class FacLista(ListView):
    """Listado de Facturas"""
    model = Factura
    template_name = 'comercial/Fac_Panel.html'
    paginate_by = 8


class FacView(DetailView):
    """Visualiza reg. Factura"""
    template_name = 'comercial/Fac_View.html'
    model = Factura


class FacNuevo(CreateView):
    """Crear Factura"""
    model = Factura
    form_class = FacturaForm
    template_name = 'comercial/Fac_New.html'
    success_url = reverse_lazy('comercial:fac_panel')

    def get_context_data(self, **kwargs):
        context = super(FacNuevo, self).get_context_data(**kwargs)
        MovinventFormset = inlineformset_factory(Factura, Movinvent, form=MovinventForm, extra=2)

        if self.request.POST:
            context['movimientos'] = MovinventFormset(self.request.POST, queryset=Movinvent.objects.select_related())
        else:
            # TODO: Hay un problema de 0n queries, debido a la generación de múltiples formset con mismo queryset, probablemente
            #       Probé con select_related sin éxito aún.
            context['movimientos'] = MovinventFormset(queryset=Movinvent.objects.select_related("mvi_cliente"))
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        movimientos = context['movimientos']
        with transaction.atomic():
            self.object = form.save()

            if movimientos.is_valid():
                # TODO: Validate per form in formset
                #       Although, formset.is_valid do this.
                # for form in movimientos:
                #     if form.is_valid():
                #         form.
                movimientos.instance = self.object
                movimientos.save()
        return super(FacNuevo, self).form_valid(form)


class FacEdita(UpdateView):
    """Actualiza Factura"""
    model = Factura
    form_class = FacturaForm
    template_name = 'comercial/Fac_Edit.html'
    success_url = reverse_lazy('comercial:fac_panel')


class FacDelet(DeleteView):
    """Elimina Factura"""
    model = Factura
    form_class = FacturaForm
    template_name = 'comercial/Fac_Delet.html'
    success_url = reverse_lazy('comercial:fac_panel')

# ========    =========== #
