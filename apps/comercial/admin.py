from django.contrib import admin

from .models import Cliente, Proveedor, Vendedor, Movinvent, Pedido, Factura

admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Vendedor)
admin.site.register(Movinvent)
admin.site.register(Pedido)
admin.site.register(Factura)