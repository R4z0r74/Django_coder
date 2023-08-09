from django.contrib import admin
from django.urls import path
from perfiles.views import *


#URL especificas de la app

urlpatterns = [ 
   # URLS Usuario y sesion
   path('registro/', registro, name="registro"),
   path('login/', login_view, name="login"),
   path('logout/', CustomLogoutView.as_view(), name="logout"),
   path('editar_mi_perfil/', MiPerfilUpdateView.as_view(), name="editar_perfil"),
   path('agregar_avatar/', agregar_avatar, name="agregar_avatar"),

   ]