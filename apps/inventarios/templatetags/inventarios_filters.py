from django import template
register = template.Library()


@register.filter(name='por_tallas')
def iterate_per_size(existencia, saldo_prefijo):
    try:
        saldoxtalla = existencia.saldoxtalla
    except Exception:
        return [('-', existencia.exs_saldact)]
    else:
        if saldoxtalla:
            for talla in range(1, 14):
                saldo = getattr(saldoxtalla, "{0}{1:02d}".format(saldo_prefijo, talla)) or 0
                talla_display = getattr(existencia.exs_idmodel.mod_tabtall, "jgo_medid{0:02d}".format(talla)) or ''
                if saldo:
                    yield (talla_display, saldo)


@register.filter(name='por_saldo')
def iterate_per_saldo(saldo):
    print(saldo)
    return [i for i in range(int(saldo))]
