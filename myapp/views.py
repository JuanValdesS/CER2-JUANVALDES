from django.shortcuts import render
from .models import Comunicado

#Lo que le podemos enviar al cliente para que lo vea por pantalla
# Create your views here.

def Inicio(request):

    comunicados = Comunicado.objects.all()

    return render(request,'Inicio.html',{
        "comunicados": comunicados
    })