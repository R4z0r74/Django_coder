from django.contrib import admin
from django.urls import path
from control_estudios.views import *
#URL especificas de la app

urlpatterns = [
path("admin/", admin.site.urls),
path("estudiantes/", listar_estudiantes),

]
