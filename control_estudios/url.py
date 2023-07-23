from django.contrib import admin
from django.urls import path
from control_estudios.views import *
#URL especificas de la app

urlpatterns = [
path("estudiantes/", listar_estudiantes, name="lista_estudiantes"),
path("cursos/", listar_cursos, name="lista_cursos"),
path('curso_formulario/', curso_formulario,  name="Curso_formulario"),
path('estudiante_formulario/', estudiante_formulario,  name="estudiante_formulario"),
path('profesor_formulario/', profesor_formulario,  name="profesor_formulario"),
path('entregable_formulario/', entregable_formulario,  name="entregable_formulario"),
path("busqueda_comision/", busqueda_comision, name="busqueda_comision"),
path("buscar/", buscar, name="buscar"),

]
