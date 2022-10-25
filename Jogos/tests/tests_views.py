from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class JogoViewTestCase(TestCase):
# criando um usuario antes de fazer o test pois a view só pode ser acessada se o usuario estiver autenticado   
    def setUp(self): 
        User.objects.create_user(username='test', email='test@test.com', password='12345678a')
        self.client.login(username='test', password='12345678a')
    
    def test_status_code_200(self):
        res = reverse("lista_jogos")
        resposta = self.client.get(res)
        self.assertEqual(resposta.status_code, 200)

    def test_template_usado(self):
        res = reverse("lista_jogos")
        resposta = self.client.get(res)
        self.assertTemplateUsed(resposta, 'jogos/jogos_list.html')

class JogoNewTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='test', email='test@test.com', password='12345678a')
        self.client.login(username='test', password='12345678a')
    
    def test_status_code_200(self):
        res = reverse("novo")
        resposta = self.client.get(res)
        self.assertEqual(resposta.status_code, 200)

    def test_template_usado(self):
        res = reverse("novo")
        resposta = self.client.get(res)
        self.assertTemplateUsed(resposta, 'jogos/jogos_form.html', msg_prefix='Não é esse Template')