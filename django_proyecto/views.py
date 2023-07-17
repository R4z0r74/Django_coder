from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render



def saludar(request):
    saludo = "Hola querido usuario"
    pagina_html = HttpResponse(saludo)
    return pagina_html

#Pasaje de parametros
def diaDeHoy(request):
    dia = datetime.now()
    documentoDeTexto = f"Hoy es dia: <br> {dia}"
    return HttpResponse(documentoDeTexto)

#Parametros desde la URL
def miNombreEs(self,nombre):
    documentoDeTexto = f"Mi nombre es: <br> {nombre}"
    return HttpResponse(documentoDeTexto)

def saludar_html(request):
    #Lo creas y lo pasas en el http_response en context. Es una forma de pasar info
    context = {
        "alumno" : "Pedro",
        "tutores": ["Jose","Maria"],
        "comision": 55212,
    }
    http_response = render(
        request=request,
        template_name="plantilla1.html",
        context=context,
    )
    return http_response