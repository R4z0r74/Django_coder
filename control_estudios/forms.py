from django import forms
 
class Curso_formulario(forms.Form):
    curso = forms.CharField()
    comision = forms.IntegerField()

class Estudiante_formulario(forms.Form):
    apellido = forms.CharField(max_length=30)
    nombre = forms.CharField(max_length=30)
    email = forms.EmailField()
    telefono = forms.CharField(max_length=20)
    dni = forms.CharField(max_length=32)
    fecha_nacimiento = forms.DateField()