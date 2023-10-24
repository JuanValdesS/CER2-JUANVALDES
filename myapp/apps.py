from django.apps import AppConfig

# Permite configurar la aplicacion

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
