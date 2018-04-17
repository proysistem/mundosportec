from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Existencia, Saldoxtalla


@receiver(post_save, sender=Existencia)
def create_saldoxtalla(sender, instance, created, **kwargs):
    if created:
        sxt = Saldoxtalla(tex_product=instance)
        sxt.save()
    #     Profile.objects.create(user=instance)


print("Se han cargado las señales de Inventarios")
