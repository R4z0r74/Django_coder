from django.test import TestCase
from django.contrib.auth.models import User

#Test de creacion de usuario
class UsuarioTests(TestCase):
    def test_creacion_usuario_y_autenticacion(self):
        # Crea un usuario de prueba
        username = 'usuario_prueba'
        password = 'contraseña'
        self.usuario = User.objects.create_user(username=username, password=password)

        # Verifica que el usuario se haya creado correctamente
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(self.usuario.username, username)

        # Prueba de autenticado exitosa
        usuario_autenticado = self.client.login(username=username, password=password)
        self.assertTrue(usuario_autenticado)

        # Prueba de autenticadofallida
        usuario_autenticado_fallido = self.client.login(username=username, password='contraseña_incorrecta')
        self.assertFalse(usuario_autenticado_fallido)
