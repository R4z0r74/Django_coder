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
from django.conf.urls.static import static
from django.conf import settings
from blog_mascotas.views import ArticuloListView




#URL GENERALES

urlpatterns = [
path("admin/", admin.site.urls),
path("", ArticuloListView.as_view(), name="pages"), #CAMBIAR PARA QUE LLEVE A LISTA_ARTICULOS
#Anexo las url de control estudios bajo el path estudios/ y perfiles bajo el path perfiles/
path("blog/",include("blog_mascotas.url")),
path("perfiles/",include("perfiles.url")),



]

#Para que carguen las imagenes bien
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    
