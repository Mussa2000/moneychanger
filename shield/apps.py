from django.apps import AppConfig


class ShieldConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "shield"
    
    # def ready(self):
    #     import shield.signals
