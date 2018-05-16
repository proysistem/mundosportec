from django import template
register = template.Library()


@register.filter(name='por_tallas')
def iterate_per_size(movimiento, saldo_prefijo):
    try:
        tab_talla = movimiento.mvi_product.exs_idmodel.mod_tabtall
    except Exception:
        raise Exception('No existe esa tabla de tallas {}'.format(str(movimiento.mvi_product.exs_idmodel.mod_tabtall)))
    else:
        for talla in range(1, 14):
            cantidadxtalla = getattr(movimiento, "{0}{1:02d}".format(saldo_prefijo, talla)) or 0
            talla_display = getattr(tab_talla, "jgo_medid{0:02d}".format(talla)) or ''
            if cantidadxtalla:
                yield (talla_display, cantidadxtalla)


@register.filter(name='por_saldo')
def iterate_per_saldo(saldo):
    return [i for i in range(int(saldo))] if saldo else []
