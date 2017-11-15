from django.contrib import admin

from .models import Cliente, Proveedor, Vendedor, Movinvent, Pedido, Factura

admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Vendedor)
admin.site.register(Pedido)
admin.site.register(Movinvent)


class MovinventInlineAdmin(admin.TabularInline):
    model = Movinvent


class FacturaAdmin(admin.ModelAdmin):
    '''
        Admin View for Factura
    '''
    inlines = [
        MovinventInlineAdmin,
    ]

admin.site.register(Factura, FacturaAdmin)
