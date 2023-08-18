from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from perfiles.forms import *
from perfiles.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def registro(request):
   if request.method == "POST":
       formulario = UserRegisterForm(request.POST)

       if formulario.is_valid():
           formulario.save()  # Esto lo puedo usar porque es un model form
           url_exitosa = reverse('pages')
           return redirect(url_exitosa)
   else:  # GET
       formulario = UserRegisterForm()
   return render(
       request=request,
       template_name='perfiles/registro.html',
       context={'form': formulario},
   )

def login_view(request):
   next_url = request.GET.get('next')
   if request.method == "POST":
       form = AuthenticationForm(request, data=request.POST)

       if form.is_valid():
           data = form.cleaned_data
           usuario = data.get('username')
           password = data.get('password')
           user = authenticate(username=usuario, password=password)
           # user puede ser un usuario o None
           if user:
               login(request=request, user=user)
               if next_url:
                   return redirect(next_url)
               url_exitosa = reverse('pages')
               return redirect(url_exitosa)
   else:  # GET
       form = AuthenticationForm()
   return render(
       request=request,
       template_name='perfiles/login.html',
       context={'form': form},
   )

class CustomLogoutView(LogoutView):
   template_name = 'perfiles/logout.html'

#Para editar datos
class MiPerfilUpdateView(LoginRequiredMixin, UpdateView):
   form_class = UserUpdateForm
   success_url = reverse_lazy('exito')
   template_name = 'perfiles/formulario_perfiles.html'

   def get_object(self, queryset=None):
       return self.request.user

@login_required
def cambiar_contrasena(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('cambiar_contrasena')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'perfiles/cambiar_contrasena.html', {'form': form})

#Pára el avatar
def agregar_avatar(request):
  if request.method == "POST":
      formulario = AvatarFormulario(request.POST, request.FILES) # Aquí me llega toda la info del formulario html

      if formulario.is_valid():
          avatar = formulario.save()
          avatar.user = request.user
          avatar.save()
          url_exitosa = reverse('pages')
          return redirect(url_exitosa)
  else:  # GET
      formulario = AvatarFormulario()
  return render(
      request=request,
      template_name="perfiles/formulario_avatar.html",
      context={'form': formulario},
  )

