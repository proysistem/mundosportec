from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()


class Usuarioform(UserCreationForm):
    """docstring for  Users"""
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
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

        # widgets = {
            # 'password': forms.PasswordInput(),
            # }
