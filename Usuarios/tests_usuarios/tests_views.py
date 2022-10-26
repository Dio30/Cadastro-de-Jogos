from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class UsuarioViewTestCase(TestCase):
    
    def test_status_code_200(self):
        res = reverse("cadastrar")
        resposta = self.client.get(res)
        self.assertEqual(resposta.status_code, 200)

    def test_template_usado(self):
        res = reverse("cadastrar")
        resposta = self.client.get(res)
        self.assertTemplateUsed(resposta, 'cadastro/cadastrar.html')

class LoginTestCase(TestCase):
    
    def test_status_code_200(self):
        res = reverse("login")
        resposta = self.client.get(res)
        self.assertEqual(resposta.status_code, 200)

    def test_template_usado(self):
        res = reverse("login")
        resposta = self.client.get(res)
        self.assertTemplateUsed(resposta, 'cadastro/login.html', msg_prefix='Não é esse Template')

class PerfilViewTest(TestCase):
    def setUp(self):
        User.objects.create_user(username='test', email='test@test.com', password='12345678a')
        self.client.login(username='test', password='12345678a')
    
    def test_status_code_200(self):
        res = reverse("perfil_edit")
        resposta = self.client.get(res)
        self.assertEqual(resposta.status_code, 200)

    def test_template_usado(self):
        res = reverse("perfil_edit")
        resposta = self.client.get(res)
        self.assertTemplateUsed(resposta, 'cadastro/perfil_edit.html', msg_prefix='Não é esse Template')

class PasswordChangeViewTest(TestCase):
    def setUp(self):
        User.objects.create_user(username='test', email='test@test.com', password='12345678a')
        self.client.login(username='test', password='12345678a')
    
    def test_status_code_200(self):
        res = reverse("trocar_senha")
        resposta = self.client.get(res)
        self.assertEqual(resposta.status_code, 200)

    def test_template_usado(self):
        res = reverse("trocar_senha")
        resposta = self.client.get(res)
        self.assertTemplateUsed(resposta, 'cadastro/trocar_senha.html', msg_prefix='Não é esse Template')