from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.contrib.auth.models import User
from blog_mascotas.models import Articulo

# Create your tests here.

# Test de articulo. Correr python manage.py test


class ArticuloTests(TestCase):
    def setUp(self):
        # Crea un usuario de prueba
        self.usuario = User.objects.create_user(username='usuario_prueba', password='contraseña')


    def test_creacion_articulo_con_imagen(self):
        # Crear imagen temporal
        imagen_de_prueba = SimpleUploadedFile(
            "imagen_prueba.jpg",
            b"contenido_de_prueba",
            content_type="image/jpeg"
        )

        # Articulo con la imagen
        articulo = Articulo.objects.create(
            autor=self.usuario,
            titulo="Título de prueba",
            subtitulo="Subtítulo de prueba",
            cuerpo="Contenido de prueba",
            fecha="2000-01-01",
            imagen=imagen_de_prueba
        )

        # Comprobar que el artículo fue creado con la imagen correctamente
        self.assertEqual(Articulo.objects.count(), 1)
        self.assertEqual(articulo.imagen.name, "imagen_prueba.jpg")

    def test_articulo_str(self):
        # Crear un artículo de prueba sin imagen
        articulo = Articulo.objects.create(
            autor=self.usuario,
            titulo="Título de prueba",
            subtitulo="Subtítulo de prueba",
            cuerpo="Contenido de prueba",
            fecha="2000-01-01"
        )

        # Comprobar que el método __str__ funciona
        self.assertEqual(articulo.__str__(), "usuario_prueba,Título de prueba,Subtítulo de prueba,Contenido de prueba,2000-01-01")


