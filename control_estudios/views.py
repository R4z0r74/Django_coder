from django.shortcuts import render
from django.http import HttpResponse
from control_estudios.models import *
from control_estudios.forms import *

# Create your views here.

def listar_estudiantes(request):
    contexto = {
        "profesor" : "Pablo",
        "estudiantes": [
        {"nombre": "Emanuel", "apellido": "Dautel", "nota":10},
        {"nombre": "Manuela", "apellido": "Gomez",  "nota":4},
        {"nombre": "Ivan", "apellido": "Tomasevich", "nota":7},
        {"nombre": "Carlos", "apellido": "Perez", "nota":2},
        ]
    }
    http_response = render(
        request=request,
        template_name= "control_estudios/listar_estudiantes.html",
        context=contexto,
    ) 
    return http_response

def listar_cursos(request):
    # Data de pruebas, más adelante la llenaremos con nuestros cursos de verdad
    contexto = {
        "cursos": [
            {"nombre": "Fisica", "comision": 1000},
            {"nombre": "Python", "comision": 55350},
            {"nombre": "Redes Sociales", "comision": 2000},
        ]
    }
    http_response = render(
        request=request,
        template_name='control_estudios/listar_cursos.html',
        context=contexto,
    )
    return http_response

 
def curso_formulario(request):
 
      if request.method == "POST":
 
            miFormulario = Curso_formulario(request.POST) # Aqui me llega la informacion del html

            print(miFormulario)
 
            if miFormulario.is_valid: #Si paso la validacion de django
                  informacion = miFormulario.cleaned_data
                  curso = Curso(nombre=informacion["curso"], comision=informacion["comision"])
                  curso.save()
                  return render(request, "control_estudios/listar_cursos.html") #Vuelve a donde uno quiera
      else:
            miFormulario = Curso_formulario() #Formulario vacio para construir el html
 
      return render(request, "control_estudios/curso_formulario.html", {"miFormulario": miFormulario})


def estudiante_formulario(request):
 
      if request.method == "POST":
 
            miFormulario = Estudiante_formulario(request.POST) # Aqui me llega la informacion del html

            print(miFormulario)
 
            if miFormulario.is_valid: #Si paso la validacion de django
                  informacion = miFormulario.cleaned_data
                  estudiante = Curso(nombre=informacion["nombre"], apellido=informacion["apellido"],email=informacion["email"],telefono=informacion["telefono"],dni=informacion["dni"],fecha_nacimiento=informacion["fecha_nacimiento"])
                  estudiante.save()
                  return render(request, "control_estudios/listar_estudiantes.html") #Vuelve a donde uno quiera
      else:
            miFormulario = Estudiante_formulario() #Formulario vacio para construir el html
 
      return render(request, "control_estudios/estudiante_formulario.html", {"miFormulario": miFormulario})




def busqueda_comision(request):
     return render(request,"control_estudios/busqueda_comision.html")

def buscar(request):
     respuesta = f"Estoy buscando la comision numero: {request.GET['comision']}"
     return HttpResponse(respuesta)
     