# Proyecto CoderHouse
## Instrucciones instalar proyecto en local
+ Crea una carpeta contenedora
+ Abre la consola y ubicate en la carpeta
+ Clona este proyecto en la carpeta
+ Entra en la carpeta que acabas de clonar
+ Para instalar las dependencias corre este comando:

```
pip install -r requirements.txt
```

## Instrucciones para entrar al panel aministrativo de Django
+ En consola, crear un superuser:
```
python manage.py createsuperuser
```
+ Correr python manage.py runserver y acceder con user y password via:
```
127.0.0.1:8000/admin
```

# Superusuario de pruebas
username: superprueba 
password: 12345

# Usuarios normales
username: usuarionormal
password: usuario9876


# Funcionalidades
## Recorda correr python manage.py runserver
El proyecto tiene las siguientes funcionalidades principales para los usuarios:

Búsqueda de Comisiones:
Permite buscar cursos por número de comisión.

Gestión de Cursos:
Crear cursos.

Gestión de Estudiantes:
Crear estudiantes.

Gestión de Profesores:
Crear profesores.

Gestión de Entregables:
Crear entregables.

El codigo de las funcionalidades se encuentra en la app de control_estudios en views.py y los html en templates.

