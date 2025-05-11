from django.apps import AppConfig


class MyFinanceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_finance'

    def ready(self):
        # Импортируем сигналы, чтобы они зарегистрировались
        from . import signals