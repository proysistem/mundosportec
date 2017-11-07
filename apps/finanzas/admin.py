from django.contrib import admin

from .models import Moneda, Cajera, Caja, Movicaja

admin.site.register(Moneda)
admin.site.register(Cajera)
admin.site.register(Caja)
admin.site.register(Movicaja)