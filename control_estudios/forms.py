from django import forms
 
class Curso_formulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    comision = forms.IntegerField(required=True, max_value=50000)

class Estudiante_formulario(forms.Form):
    apellido = forms.CharField(required=True, max_length=32)
    nombre = forms.CharField(required=True, max_length=32)
    email = forms.EmailField()
    telefono = forms.CharField(max_length=20)
    dni = forms.CharField(max_length=32)
    fecha_nacimiento = forms.DateField()

class Profesor_formulario(forms.Form):
    apellido = forms.CharField(required=True, max_length=32)
    nombre = forms.CharField(required=True, max_length=32)
    dni = forms.CharField(required=True, max_length=32)
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField()
    profesion = forms.CharField(max_length=32)
    bio = forms.CharField(max_length=256)


class Entregable_formulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=32)
    fecha_entrega = forms.DateTimeField()
    esta_aprobado = forms.BooleanField(required=True) 