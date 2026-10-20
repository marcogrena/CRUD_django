from django.apps import AppConfig


class ProdottiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    # Percorso completo del pacchetto: serve a Django per registrarla in INSTALLED_APPS
    name = "hello_world.prodotti"
