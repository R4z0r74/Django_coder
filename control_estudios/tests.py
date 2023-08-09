from django.test import TestCase
from control_estudios.models import Curso

# Create your tests here.

#Test de curso. Correr python manage.py test
class CursoTests(TestCase):
   """En esta clase van todas las pruebas del modelo Curso."""

   def test_creacion_curso(self):
       # caso uso esperado
       curso = Curso(nombre="Titulo", comision=1000)
       curso.save()

       # Compruebo que el curso fue creado y la data fue guardada correctamente
       self.assertEqual(Curso.objects.count(), 1)
       self.assertEqual(curso.nombre, "Titulo")
       self.assertEqual(curso.comision, 1000)

   def test_curso_str(self):
       curso = Curso(nombre="Python", comision=20000) #No registra la comision
       curso.save()

       # Compruebo el str funciona como se desea
       self.assertEqual(curso.__str__(), "Python, 20000")
