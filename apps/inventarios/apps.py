from django.apps import AppConfig


class InventariosConfig(AppConfig):
    name = 'apps.inventarios'

    def ready(self):
        import apps.inventarios.signals
