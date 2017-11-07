from django.contrib import admin

from .models import Pais, Provincia, Ciudad, Zipcodigo, Sucursal, Categoria, Tipomovim, Motivo

admin.site.register(Pais)
admin.site.register(Provincia)
admin.site.register(Ciudad)
admin.site.register(Zipcodigo)
admin.site.register(Sucursal)
admin.site.register(Categoria)
admin.site.register(Tipomovim)
admin.site.register(Motivo)