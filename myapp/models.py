from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Entidad(models.Model):
    #Se asigna el id como automatico y como primary key en True
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombre

    Logo = models.ImageField

class Comunicado(models.Model):
    id = models.BigAutoField(primary_key=True)

    #Opciones dentro del tipo_choices
    TIPOS = [("S","Suspensión de actividades"), ("C","Suspensión de clases"), ("I","Información")]

    titulo = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.titulo
    
    detalle = models.CharField(max_length=500)
    detalle_corto = models.CharField(max_length=250)
    tipo = models.CharField(max_length=30, choices=TIPOS)
    #entidad es clave foranea hacia el modelo Entidad. el models.CASCADE dice que si el objeto relacionado se elimina, el objeto que contiene la clave foránea tambien se elimina automáticamente
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    #BooleanField almacena valores booleanos que pueden ser verdaderos o falsos, si o no, publico o no publico, etc. En este caso indica que el campo no esta visible
    visible = models.BooleanField(default=False)
    #DateTimeField(auto_now_add=True) con este campo estamos especificando que apenas se cree el objeto, se le especificará la hora automaticamente en el momento de la creacion.
    #Sirve para tener seguimiento de los registros en la base de datos. no cambiará la fecha despues de creado el objeto
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    #El campo se actualizará automáticamente con la fecha y hora actual cada vez que se modifique el objeto en la(sin add)
    fecha_ultima_modificacion = models.DateTimeField(auto_now=True)
    #related_name especifica el nombre que se utilizará para acceder a los objetos relacionados desde el modelo User.
    publicado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comunicados_publicados')
    modificado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comunicados_modificados')