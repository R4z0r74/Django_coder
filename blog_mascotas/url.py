from django.contrib import admin
from django.urls import path, include
from blog_mascotas.views import *
#Para incluir los archivos media
from django.conf import settings
from django.conf.urls.static import static

#URL especificas de la app

urlpatterns = [
path('about/', about, name="about"),
path('articulo_formulario/', articulo_formulario, name="articulo_formulario"),
path("exito/", exito, name="exito"),

# URLS de estudiantes
path("pages/", ArticuloListView.as_view(), name="pages"),
path('articulo_autor', articulo_autor, name="articulos_autor"),
path('pages/<int:pk>/', ArticuloDetailView.as_view(), name="detalle_articulo"), 
path('crear_articulo/', ArticuloCreateView.as_view(), name="crear_articulo"),
path('editar_articulo/<int:pk>/', ArticuloUpdateView.as_view(), name="editar_articulo"),
path('borrar_articulo/<int:pk>/', ArticuloDeleteView.as_view(), name="borrar_articulo"),
path('post_propios/', post_propios, name="post_propios"),



]


#Sirve para incluir los archivos media: imagenes, etc
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
