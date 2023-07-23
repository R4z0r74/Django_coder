from django.contrib import admin
from django.urls import path
from control_estudios.views import *
#URL especificas de la app

urlpatterns = [
path('curso_formulario/', curso_formulario,  name="curso_formulario"),
path('estudiante_formulario/', estudiante_formulario,  name="estudiante_formulario"),
path('profesor_formulario/', profesor_formulario,  name="profesor_formulario"),
path('entregable_formulario/', entregable_formulario,  name="entregable_formulario"),
path("busqueda_comision/", busqueda_comision, name="busqueda_comision"),
path("buscar/", buscar, name="buscar"),

]
