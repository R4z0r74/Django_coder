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
path("exito/", exito, name="exito"),
path("listar_cursos/", listar_cursos, name="listar_cursos"),
path("eliminar_curso//<int:id>/", eliminar_curso, name="eliminar_curso"),
path('editar_curso/<int:id>/', editar_curso, name="editar_curso"),
# URLS de estudiantes
path("estudiantes/", EstudianteListView.as_view(), name="lista_estudiantes"),
path('estudiantes/<int:pk>/', EstudianteDetailView.as_view(), name="ver_estudiante"),
path('crear_estudiante/', EstudianteCreateView.as_view(), name="crear_estudiante"),
path('editar_estudiante/<int:pk>/', EstudianteUpdateView.as_view(), name="editar_estudiante"),
path('eliminar_estudiante/<int:pk>/', EstudianteDeleteView.as_view(), name="eliminar_estudiante"),

]
