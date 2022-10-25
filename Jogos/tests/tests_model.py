from django.test import TestCase
from ..models import Jogos
from django.contrib.auth.models import User

class JogosTest(TestCase):
    def setUp(self):
        users= User.objects.create(username='dione')
        Jogos.objects.create(
            nome_do_jogo='fifa',
            estilo_do_jogo='Ação',
            imagem = 'static/imagens/74472.png',
            usuario = users
        )
    
    def test_return_str(self):
        jogo = Jogos.objects.get(nome_do_jogo='fifa')
        self.assertEqual(jogo.__str__(), 'fifa')