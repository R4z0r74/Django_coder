from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Articulo(models.Model):
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    titulo = models.CharField(max_length=256)
    subtitulo = models.CharField(max_length=256)
    cuerpo = models.CharField(max_length=5656) #RichTextField 
    fecha = models.DateField()

    def __str__(self):
        return f"{self.autor},{self.titulo},{self.subtitulo},{self.cuerpo},{self.fecha}"
    




