from django.views.generic import CreateView
from .models import User
from .forms import Usuarioform
from django.core.unresolvers import reverse_lazy


class UsrNuevo(CreateView):
    """Listado de Usuarios"""
    form_class = Usuarioform
    model = User
    template_name = 'usuarios/Usr_New.html'
    success_url = reverse_lazy('users:usr_new')
