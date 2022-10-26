from typing import IO
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Jogos
import json

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
        self.user= User.objects.create(username='dione')
        self.res = reverse("novo")
        self.jogo1 = Jogos.objects.create(
            nome_do_jogo='jogo1',
            estilo_do_jogo = 'Ação',
            imagem = 'static/imagens/74472.png',
            usuario=self.user
            )
    
    def test_status_code_200_get(self):
        resposta = self.client.get(self.res)
        self.assertEquals(resposta.status_code, 200)
        self.assertTemplateUsed(resposta, 'jogos/jogos_form.html', msg_prefix='Não é esse Template')
    
    def test_status_code_200_post(self):
        resposta = self.client.post(self.res, {
            'nome_do_jogo': 'jogo1',
            'estilo_do_jogo': 'Ação',
            'imagem': 'static/imagens/74472.png',
            'usuario': self.user
        })
        self.assertEquals(resposta.status_code, 200)
        self.assertEquals(self.jogo1.nome_do_jogo.title().lower(), 'jogo1')

class JogoEditTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='test', email='test@test.com', password='12345678a')
        self.client.login(username='test', password='12345678a')
        self.user= User.objects.create(username='dione')
        self.jogo1 = Jogos.objects.create(
            nome_do_jogo='jogo1',
            estilo_do_jogo = 'Ação',
            imagem = 'static/imagens/74472.png',
            usuario=self.user
            )
        self.res = reverse("novo")
        
    def test_status_code_200_put(self):
        resposta = self.client.put(self.res, {
            'nome_do_jogo': 'jogo2',
            'estilo_do_jogo': 'Aventura',
            'imagem': 'static/imagens/74472.png',
            'usuario': self.user
        })
        self.assertEquals(resposta.status_code, 200)
        self.assertTemplateUsed(resposta, 'jogos/jogos_form.html', msg_prefix='Não é esse Template')

class JogoDeleteTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='dione')
        self.jogo1 = Jogos.objects.create(
            nome_do_jogo='jogo1',
            estilo_do_jogo = 'Ação',
            imagem = 'static/imagens/74472.png',
            usuario=user
            )
        self.res = reverse("deletar", kwargs={'pk':self.jogo1.pk})
    
    def test_status_code_204_delete(self):
        resposta = self.client.delete(self.res)
        self.assertEquals(resposta.status_code, 302)