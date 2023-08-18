from django.contrib import admin
from django.urls import path
from perfiles.views import *


#URL especificas de la app

urlpatterns = [ 
   # URLS Usuario y sesion
   path('accounts/signup/', registro, name="registro"), 
   path('accounts/login/', login_view, name="login"),
   path('logout/', CustomLogoutView.as_view(), name="logout"),
   path('accounts/profile/', MiPerfilUpdateView.as_view(), name="editar_perfil"), 
   path('cambiar_contrasena/', cambiar_contrasena, name='cambiar_contrasena'),
   path('agregar_avatar/', agregar_avatar, name="agregar_avatar"),


   ]

