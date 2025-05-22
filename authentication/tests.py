from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword123'
        )
        
    def test_login_view(self):
        """Prueba que la vista de login funcione correctamente"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/login.html')
        
        # Prueba de login con credenciales correctas
        login_data = {
            'username': 'testuser',
            'password': 'testpassword123'
        }
        response = self.client.post(reverse('login'), login_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)
        
        # Logout para la siguiente prueba
        self.client.logout()
        
        # Prueba de login con credenciales incorrectas
        login_data = {
            'username': 'testuser',
            'password': 'wrongpassword'
        }
        response = self.client.post(reverse('login'), login_data)
        self.assertEqual(response.status_code, 200)
        # Verificamos que el formulario tenga errores en lugar de verificar el estado de autenticación
        self.assertTrue(response.context['form'].errors)
        
    def test_register_view(self):
        """Prueba que la vista de registro funcione correctamente"""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/register.html')
        
        # Prueba de registro con datos válidos
        register_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newpassword123',
            'password2': 'newpassword123'
        }
        response = self.client.post(reverse('register'), register_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(username='newuser').exists())
        
    def test_profile_view(self):
        """Prueba que la vista de perfil requiera autenticación y muestre el template correcto"""
        # Intento de acceso sin autenticación
        response = self.client.get(reverse('profile'))
        self.assertNotEqual(response.status_code, 200)
        
        # Acceso con autenticación
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/profile.html')
        
    def test_logout_view(self):
        """Prueba que la vista de logout funcione correctamente"""
        # Login primero
        self.client.login(username='testuser', password='testpassword123')
        
        # Luego logout
        response = self.client.get(reverse('logout'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_authenticated)
