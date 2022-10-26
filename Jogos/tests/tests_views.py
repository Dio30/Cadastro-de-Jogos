from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Jogos

class JogoViewTestCase(TestCase):
# criando um usuario antes de fazer o test pois a view só pode ser acessada se o usuario estiver autenticado   
    def setUp(self): 
        User.objects.create_user(username='test', email='test@test.com', password='12345678a')
        self.client.login(username='test', password='12345678a')
    
    def test_status_code_200(self):
        res = reverse("lista_jogos")
        resposta = self.client.get(res)
        self.assertEqual(resposta.status_code, 200)
        self.assertTemplateUsed(resposta, 'jogos/jogos_list.html')

class JogoNewTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='test', email='test@test.com', password='12345678a')
        self.client.login(username='test', password='12345678a')
        user= User.objects.create(username='dione')
        self.res = reverse("novo")
        self.jogo1 = Jogos.objects.create(
            nome_do_jogo='jogo1',
            estilo_do_jogo = 'Ação',
            imagem = 'static/imagens/74472.png',
            usuario=user
            )
    
    def test_status_code_200_get(self):
        res = reverse("novo")
        resposta = self.client.get(res)
        self.assertEquals(resposta.status_code, 200)
        self.assertTemplateUsed(resposta, 'jogos/jogos_form.html', msg_prefix='Não é esse Template')
    
    def test_status_code_200_post(self):
        resposta = self.client.post(self.res, self.jogo1)
        self.assertEquals(resposta.status_code, 200)
        self.assertTemplateUsed(resposta, 'jogos/jogos_form.html', msg_prefix='Não é esse Template')
        
class JogoEditTestCase(TestCase): #terminar
    def setUp(self):
        User.objects.create_user(username='test', email='test@test.com', password='12345678a')
        self.client.login(username='test', password='12345678a')
        user= User.objects.create(username='dione')
        self.jogo1 = Jogos.objects.create(
            nome_do_jogo='jogo1',
            estilo_do_jogo = 'Ação',
            imagem = 'static/imagens/74472.png',
            usuario=user
            )
        
    def test_status_code_200(self):
        res = reverse("editar", args=['jogo1'])
        resposta = self.client.get(res)
        self.assertEquals(resposta.status_code, 200)
        self.assertTemplateUsed(resposta, 'jogos/jogos_form.html', msg_prefix='Não é esse Template')
    
    def test_status_code_302(self):
        res = reverse("editar", args=['jogo1'])
        resposta = self.client.put(res, self.jogo1)
        self.assertEquals(resposta.status_code, 302)
        self.assertTemplateUsed(resposta, 'jogos/jogos_form.html', msg_prefix='Não é esse Template')
        
class JogoDeleteTestCase(TestCase): #terminar
    def setUp(self):
        User.objects.create_user(username='test', email='test@test.com', password='12345678a')
        self.client.login(username='test', password='12345678a')
        user= User.objects.create(username='dione')
        self.jogo1 = Jogos.objects.create(
            nome_do_jogo='jogo1',
            estilo_do_jogo = 'Ação',
            imagem = 'static/imagens/74472.png',
            usuario=user
            )
      
    def test_status_code_204(self):
        user = reverse('deletar', args=['jogo1'])
        resposta = self.client.delete(user, self.jogo1)
        self.assertEquals(resposta.status_code, 204)