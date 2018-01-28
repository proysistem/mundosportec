from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Usuarioform(UserCreationForm):
    """docstring for  Users"""
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'sucursal',
            'telefono',
            'celular',
            'picture_user',
            'is_active',
            'is_staff',
            ]
        labels = {
            'username':  'Usuario',
            'email':  'Email',
            'first_name':  'Nombre',
            'last_name':  'Apellido',
            'sucursal':  'Sucursal',
            'telefono':  'Telefono',
            'celular':  'Celular',
            'picture_user':  'Foto',
            'is_active':  'Activo',
            'is_staff':  'Staf',
            }
