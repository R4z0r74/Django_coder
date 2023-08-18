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
password: superusuario

# Usuarios normales
username: prueba
password: usuarioprueba


# Funcionalidades
## Recorda correr python manage.py runserver
El proyecto tiene las siguientes funcionalidades principales para los usuarios:

Gestión de Articulos:
Crear Articulos,
Editar Articulos,
Borrar Articulos

Gestión de Perfiles:
Crear Perfiles,
Editar Perfiles.

El codigo de las funcionalidades se encuentra en la app de control_estudios en views.py, perfiles views.py y los html en templates.

Link del video demostrativo: https://www.awesomescreenshot.com/video/20031585?key=793f64f71a8b8c62f9d081c74fb82618