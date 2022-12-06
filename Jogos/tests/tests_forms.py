from django.test import TestCase
from ..forms import JogosForm
from django.contrib.auth.models import User

class JogosFormTest(TestCase):
    def test_jogos_form_valido(self):
        user= User.objects.create(username='dione')
        form = JogosForm(data={
            'nome_do_jogo':'fifa',
            'estoque':"1",
            'estilo_do_jogo':'Ação',
            'imagem': 'static/imagens/74472.png',
            "usuario": user,
        })
        self.assertTrue(form.is_valid())
    
    def test_jogos_form_invalido(self): #para saber se acontece erro no form com os dados vazios, se estiver retorna True
        form = JogosForm(data={})
        self.assertFalse(form.is_valid())