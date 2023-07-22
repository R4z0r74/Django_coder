from django.shortcuts import render

# Create your views here.

def listar_estudiantes(request):
    contexto = {
        "profesor" : "Pablo",
        "estudiantes": [
        {"nombre": "Emanuel", "apellido": "Dautel", "nota":10},
        {"nombre": "Manuela", "apellido": "Gomez",  "nota":4},
        {"nombre": "Ivan", "apellido": "Tomasevich", "nota":7},
        {"nombre": "Carlos", "apellido": "Perez", "nota":2},
        ]
    }
    http_response = render(
        request=request,
        template_name= "control_estudios/listar_estudiantes.html",
        context=contexto,
    ) 
    return http_response

def listar_cursos(request):
    # Data de pruebas, más adelante la llenaremos con nuestros cursos de verdad
    contexto = {
        "cursos": [
            {"nombre": "Fisica", "comision": 1000},
            {"nombre": "Python", "comision": 55350},
            {"nombre": "Redes Sociales", "comision": 2000},
        ]
    }
    http_response = render(
        request=request,
        template_name='control_estudios/listar_cursos.html',
        context=contexto,
    )
    return http_response