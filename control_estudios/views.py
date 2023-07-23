from django.shortcuts import render
from django.http import HttpResponse
from control_estudios.models import *
from control_estudios.forms import *

# Create your views here.

def curso_formulario(request):
 
      if request.method == "POST":
 
            miFormulario = Curso_formulario(request.POST) # Aqui me llega la informacion del html

            print(miFormulario)
 
            if miFormulario.is_valid(): #Si paso la validacion de django
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
 
            if miFormulario.is_valid(): #Si paso la validacion de django
                  informacion = miFormulario.cleaned_data
                  estudiante = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"],email=informacion["email"],telefono=informacion["telefono"],dni=informacion["dni"], fecha_nacimiento=informacion["fecha_nacimiento"])
                  estudiante.save()
                  return render(request, "control_estudios/listar_estudiantes.html") #Vuelve a donde uno quiera
      else:
            miFormulario = Estudiante_formulario() #Formulario vacio para construir el html
 
      return render(request, "control_estudios/estudiante_formulario.html", {"miFormulario": miFormulario})

def profesor_formulario(request):
 
      if request.method == "POST":
 
            miFormulario = Profesor_formulario(request.POST) # Aqui me llega la informacion del html

            print(miFormulario)
 
            if miFormulario.is_valid(): #Si paso la validacion de django
                  informacion = miFormulario.cleaned_data
                  estudiante = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"],email=informacion["email"],dni=informacion["dni"], fecha_nacimiento=informacion["fecha_nacimiento"],profesion=informacion["profesion"],bio=informacion["bio"])
                  estudiante.save()
                  return render(request, "control_estudios/listar_estudiantes.html") #Vuelve a donde uno quiera
      else:
            miFormulario = Profesor_formulario() #Formulario vacio para construir el html
 
      return render(request, "control_estudios/profesor_formulario.html", {"miFormulario": miFormulario})


def entregable_formulario(request):
 
      if request.method == "POST":
 
            miFormulario = Entregable_formulario(request.POST) # Aqui me llega la informacion del html

            print(miFormulario)
 
            if miFormulario.is_valid(): #Si paso la validacion de django
                  informacion = miFormulario.cleaned_data
                  estudiante = Entregable(nombre=informacion["nombre"], fecha_entrega=informacion["fecha_entrega"],esta_aprobado=informacion["esta_aprobado"])
                  estudiante.save()
                  return render(request, "control_estudios/listar_estudiantes.html") #Vuelve a donde uno quiera
      else:
            miFormulario = Entregable_formulario() #Formulario vacio para construir el html
 
      return render(request, "control_estudios/profesor_formulario.html", {"miFormulario": miFormulario})







def busqueda_comision(request):
     
     return render(request,"control_estudios/busqueda_comision.html")

def buscar(request):

     
      if request.GET["comision"]:
            respuesta = f"Estoy buscando la comision numero: {request.GET['comision']}"
            comision = request.GET["comision"]
            cursos=Curso.objects.filter(comision_icontains=comision)

            return render(request, "control_estudios/inicio.html", {"cursos":cursos, "comision":comision})
      else:
            respuesta = "No enviaste datos"

      return render(request,"control_estudios/inicio.html",{"respuesta":respuesta})
     