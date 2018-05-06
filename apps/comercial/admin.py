from django.contrib import admin

from .models import (Cliente, Proveedor, Vendedor, Movinvent, Pedido, Factura, Compra, Ajustecr,
                     Notacred)

admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Vendedor)
admin.site.register(Compra)
admin.site.register(Factura)
admin.site.register(Ajustecr)
admin.site.register(Notacred)
admin.site.register(Movinvent)


class MovinventInlineAdmin(admin.TabularInline):
    model = Movinvent


class PedidoAdmin(admin.ModelAdmin):
    '''
        Admin View for Factura
    '''
    inlines = [
        MovinventInlineAdmin,
    ]

admin.site.register(Pedido, PedidoAdmin)
# admin.site.register(Factura, FacturaAdmin)
