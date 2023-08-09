from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Curso(models.Model):
# los atributos de clase (son las columnas de la tabla)
    nombre = models.CharField(max_length=64)
    comision = models.IntegerField()
    #Sirve para relacionar dos modelos, en esta caso user y curso. Hay que hacer makemigrations y borrar la base de datos para modificar. 
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) #Ver tambiem de sacar set null por cascade y el null = true
    
    def __str__(self):
        return f"{self.nombre}, {self.comision}"

class Estudiante(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField(null=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Profesor(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField(blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    profesion = models.CharField(max_length=128)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"


class Entregable(models.Model):
    nombre = models.CharField(max_length=256)
    fecha_entrega = models.DateTimeField(auto_now_add=True)
    esta_aprobado = models.BooleanField(default=False) 

    def __str__(self):
        return f"{self.nombre}"
