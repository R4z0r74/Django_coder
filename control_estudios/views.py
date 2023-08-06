from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from control_estudios.models import *
from control_estudios.forms import *
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


# Create your views here.

def curso_formulario(request):
    if request.method == "POST":
        # Creo un objeto formulario con la data que envio el usuario
        formulario = Curso_formulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            #Una manera de hacerlo *
            nombre = data["nombre"]
            comision = data["comision"]
            curso = Curso(nombre=nombre, comision=comision)
            curso.save()
            # Redirecciono al usuario a la lista de cursos
            url_exitosa = reverse('estudios/listar_cursos/')
            return redirect(url_exitosa)
        
    else:  # GET
        formulario = Curso_formulario()
    http_response = render(
        request=request,
        template_name='control_estudios/curso_formulario.html',
        context={'formulario': formulario}
    )
    return http_response



def estudiante_formulario(request):
 
      if request.method == "POST":
 
            miFormulario = Estudiante_formulario(request.POST) # Aqui me llega la informacion del html

            print(miFormulario)
 
            if miFormulario.is_valid(): #Si paso la validacion de django
                  informacion = miFormulario.cleaned_data
                  #Otra manera de hacerlo *
                  estudiante = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"],email=informacion["email"],telefono=informacion["telefono"],dni=informacion["dni"], fecha_nacimiento=informacion["fecha_nacimiento"])
                  estudiante.save()
                  return render(request, "control_estudios/exito.html") #Vuelve a donde uno quiera
      else: # GET
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
                  return render(request, "control_estudios/exito.html") #Vuelve a donde uno quiera
      else: # GET
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
                  return render(request, "control_estudios/exito.html") #Vuelve a donde uno quiera
      else: # GET
            miFormulario = Entregable_formulario() #Formulario vacio para construir el html
 
      return render(request, "control_estudios/entregable_formulario.html", {"miFormulario": miFormulario})

def busqueda_comision(request):
     
     return render(request,"control_estudios/busqueda_comision.html")


def buscar(request):
    comision = request.GET.get("comision", "")
    
    if comision:
        cursos = Curso.objects.filter(comision__icontains=comision)
        if cursos.exists():
            return render(request, "control_estudios/busqueda_comision.html", {"cursos": cursos, "comision": comision})
        else:
            mensaje_error = f"No se encontraron cursos para la comisión: {comision}"
            return render(request, "control_estudios/busqueda_comision.html", {"mensaje_error": mensaje_error})
    else:
        mensaje_error = "No se proporcionó ninguna comisión para buscar"
        return render(request, "control_estudios/busqueda_comision.html", {"mensaje_error": mensaje_error})


def exito(request):
    return render(request, "control_estudios/exito.html")

def listar_cursos(request):
   contexto = {
       "cursos": Curso.objects.all(),
   }
   http_response = render(
       request=request,
       template_name='control_estudios/listar_cursos.html',
       context=contexto,
   )
   return http_response

def eliminar_curso(request, id):
   curso = Curso.objects.get(id=id) #Obtienes el curso de la BD
   if request.method == "POST":
       curso.delete()
       url_exitosa = reverse('listar_cursos') #Vuelve a donde uno quiera
       return redirect(url_exitosa)

   
def editar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        miformulario = Curso_formulario(request.POST)

        if miformulario.is_valid():
            data = miformulario.cleaned_data
            curso.nombre = data['nombre']
            curso.comision = data['comision']
            curso.save()
            url_exitosa = reverse('listar_cursos')
            return redirect(url_exitosa)
        
    else:  # GET
        inicial = {
            'nombre': curso.nombre,
            'comision': curso.comision,
        }
        miformulario = Curso_formulario(initial=inicial)
    return render(
        request=request,
        template_name='control_estudios/curso_formulario.html',
        context={'formulario': miformulario},
    )
  
#VISTAS BASADAS EN CLASES

class EstudianteListView(ListView): #Vista de lista
   model = Estudiante
   template_name = 'control_estudios/lista_estudiantes.html'

class EstudianteCreateView(CreateView):#CREATE vista
   model = Estudiante
   fields = ('apellido', 'nombre', 'email', "telefono", 'dni', "fecha_nacimiento")
   success_url = reverse_lazy('lista_estudiantes') #Es al url que se va a diriguir si la accion fue exitosa

class EstudianteDetailView(DetailView): #Vista detallada
   model = Estudiante
   success_url = reverse_lazy('lista_estudiantes') #Es al url que se va a diriguir si la accion fue exitosa

class EstudianteUpdateView(UpdateView): #UPDATE vista
   model = Estudiante
   fields = ('apellido', 'nombre', 'email', "telefono", 'dni', "fecha_nacimiento")
   success_url = reverse_lazy('lista_estudiantes') #Es al url que se va a diriguir si la accion fue exitosa

class EstudianteDeleteView(DeleteView): #Delete vista
   model = Estudiante
   success_url = reverse_lazy('lista_estudiantes') #Es al url que se va a diriguir si la accion fue exitosa