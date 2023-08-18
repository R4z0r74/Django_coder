from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from blog_mascotas.models import *
from blog_mascotas.forms import *
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.


@login_required
def articulo_formulario(request):
 
      if request.method == "POST":
 
            miFormulario = Articulo_formulario(request.POST) # Aqui me llega la informacion del html

            print(miFormulario)
 
            if miFormulario.is_valid(): #Si paso la validacion de django
                  informacion = miFormulario.cleaned_data
                  autor = request.user
                  #Otra manera de hacerlo *
                  articulo = Articulo(titulo=informacion["titulo"], subtitulo=informacion["subtitulo"],cuerpo=informacion["cuerpo"],autor = autor,fecha=informacion["fecha"])
                  articulo.save()
                  return render(request, "control_estudios/exito.html") #Vuelve a donde uno quiera
      else: # GET
            miFormulario = Articulo_formulario() #Formulario vacio para construir el html
 
      return render(request, "control_estudios/articulo_formulario.html", {"miFormulario": miFormulario})

def about(request):
     
     return render(request,"control_estudios/about.html")


def exito(request):
    return render(request, "control_estudios/exito.html")

# Usas el @login_required para resitrigir el acceso
@login_required
def articulo_autor(request):
    contexto = {
        "articulo": Articulo.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='articulo_autor',
        context=contexto,
    )
    return http_response

#VISTAS BASADAS EN CLASES
# LoginRequiredMixin proteje como el login_required
class ArticuloListView(ListView): #Vista
   model = Articulo 
   template_name = 'control_estudios/lista_articulos.html' 

class ArticuloCreateView(LoginRequiredMixin, CreateView):#CREATE vista
   model = Articulo
   fields = ('titulo', 'subtitulo', 'cuerpo', "autor", 'fecha')
   success_url = reverse_lazy('control_estudios/articulo_formulario') #Es al url que se va a diriguir si la accion fue exitosa

class ArticuloDetailView(DetailView):  # Vista detallada
    model = Articulo
    template_name = 'control_estudios/detalle_articulo.html'
    # Es al url que se va a diriguir si la accion fue exitosa
    success_url = reverse_lazy('control_estudios/detalle_articulo')

class ArticuloUpdateView(LoginRequiredMixin, UpdateView):  # UPDATE vista
    model = Articulo
    template_name = 'control_estudios/editar_articulo.html'
    fields = ('titulo', 'subtitulo', 'cuerpo','fecha')
    # Es al url que se va a diriguir si la accion fue exitosa
    success_url = reverse_lazy('post_propios')

class ArticuloDeleteView(LoginRequiredMixin, DeleteView):  # Delete vista
    model = Articulo
    template_name = 'control_estudios/borrar_ariticulo.html'
    # Es al url que se va a diriguir si la accion fue exitosa
    success_url = reverse_lazy('pages')

@login_required
def post_propios(request):
    user = request.user
    articulo = Articulo.objects.filter(autor=user)
    context = {'articulo': articulo}
    return render(request, 'control_estudios/post_propios.html', context)
