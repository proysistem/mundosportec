from django.contrib import admin

from .models import Tipoproducto, Unidad, Tabtalla, Division, Marca, Modelo, Color, Existencia, Saldoxtalla

admin.site.register(Tipoproducto)
admin.site.register(Unidad)
admin.site.register(Tabtalla)
admin.site.register(Division)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Color)


class ExistenciaAdmin(admin.ModelAdmin):
    readonly_fields = ('exs_product', 'exs_detalle',)

admin.site.register(Existencia, ExistenciaAdmin)
admin.site.register(Saldoxtalla)
