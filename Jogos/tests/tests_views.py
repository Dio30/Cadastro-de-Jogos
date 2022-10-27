from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Jogos

class JogoListViewTestCase(TestCase):
# criando um usuario antes de fazer o test pois a view só pode ser acessada se o usuario estiver autenticado   
    def setUp(self): 
        User.objects.create_user(username='test', email='test@test.com', password='12345678a')
        self.client.login(username='test', password='12345678a')
        
    # testando se o usuario cadastrado está conseguindo listar jogos e se o template utilizado está correto
    def test_status_code_list(self): 
        res = reverse("lista_jogos")
        resposta = self.client.get(res)
        self.assertEqual(resposta.status_code, 200)
        self.assertTemplateUsed(resposta, 'jogos/jogos_list.html')

class JogoNewViewTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='test', email='test@test.com', password='12345678a')
        self.client.login(username='test', password='12345678a')
        self.user= User.objects.get(username='test')
        self.jogo1 = Jogos.objects.create(
            nome_do_jogo='jogo1',
            estilo_do_jogo = 'Ação',
            imagem = 'static/imagens/74472.png',
            usuario=self.user
            )
        self.res = reverse("novo")

    # testando se a requisição post está sendo solicitada ao servidor
    def test_status_code_200_get_post(self):
        resposta = self.client.get(self.res)
        self.assertEqual(resposta.status_code, 200)
        self.assertTemplateUsed(resposta, 'jogos/jogos_form.html', msg_prefix='Não é esse Template')
        
    # testando se o usuario cadastrado está conseguindo postar um jogo e se o template utilizado está correto
    def test_status_code_post(self):
        resposta = self.client.post(self.res)
        self.assertEqual(resposta.status_code, 200)
        self.assertTemplateUsed(resposta, 'jogos/jogos_form.html', msg_prefix='Não é esse Template')

class JogoEditTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='test', email='test@test.com', password='12345678a')
        self.client.login(username='test', password='12345678a')
        self.user= User.objects.get(username='test')
        self.jogo1 = Jogos.objects.create(
            nome_do_jogo='jogo1',
            estilo_do_jogo = 'Ação',
            imagem = 'static/imagens/74472.png',
            usuario=self.user
            )
        self.res = reverse("editar", kwargs={'pk':self.jogo1.pk})
    
    # testando se a requisição put está sendo solicitada ao servidor
    def test_status_code_200_get_put(self):
        resposta = self.client.get(self.res)
        self.assertEqual(resposta.status_code, 200)
        self.assertTemplateUsed(resposta, 'jogos/jogos_form.html', msg_prefix='Não é esse Template')
        
    # testando se o usuario cadastrado está conseguindo editar um jogo e se o template utilizado está correto  
    def test_status_code_put(self):
        resposta = self.client.put(self.res, data={
            'nome_do_jogo':'jogo2',
            'estilo_do_jogo ': 'Aventura',
            'imagem' : 'static/imagens/74472.png',
            'usuario': self.user
            })
        self.assertEqual(resposta.status_code, 200)
        self.assertTemplateUsed(resposta, 'jogos/jogos_form.html', msg_prefix='Não é esse Template')

class JogoDeleteTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='test', email='test@test.com', password='12345678a')
        self.client.login(username='test', password='12345678a')
        user = User.objects.get(username='test')
        self.jogo1 = Jogos.objects.create(
            nome_do_jogo='jogo1',
            estilo_do_jogo = 'Ação',
            imagem = 'static/imagens/74472.png',
            usuario=user
            )
        self.res = reverse("deletar", kwargs={'pk':self.jogo1.pk})
        
    # testando se o usuario cadastrado está conseguindo deletar um jogo
    def test_status_code_delete(self):
        resposta = self.client.delete(self.res, data={'id': 1}, follow=True)
        self.assertEqual(resposta.status_code, 200)