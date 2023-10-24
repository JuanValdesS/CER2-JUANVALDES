from django.contrib import admin
#importamos los modelos de entidad y comunicado al administrador de django
from .models import Entidad, Comunicado



# Permite registrar usuarios con determinados rol y demás

#añadimos el registro
admin.site.register(Entidad)
admin.site.register(Comunicado)
