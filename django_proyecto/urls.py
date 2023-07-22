"""
URL configuration for django_proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django_proyecto.views import *
#URL GENERALES

urlpatterns = [
path("admin/", admin.site.urls),
path("", inicio, name="inicio"),

#Anexo las url de control estudios bajo el path estudios/
path("estudios/",include("control_estudios.url")),


#Path de pracitca
#path("inicio/", saludar),
#path("diaDeHoy", diaDeHoy),
#path("miNombreEs/<nombre>", miNombreEs),


]
