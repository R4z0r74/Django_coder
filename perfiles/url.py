from django.contrib import admin
from django.urls import path
from perfiles.views import *

#URL especificas de la app

urlpatterns = [ 
   # URLS Usuario y sesion
   path('registro/', registro, name="registro"),
   path('login/', login_view, name="login"),
   path('logout/', CustomLogoutView.as_view(), name="logout"),

   ]