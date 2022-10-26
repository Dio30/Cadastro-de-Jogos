from django.test import TestCase
from django.contrib.auth.models import User

class UsuariosFormTest(TestCase):
    
    def test_usuario_form_valido(self):
        User.objects.create_user(
            username='teste10',
            email='texto@exemplo.com',
            password= 'exemplo1234',
        )
        resposta = self.client.login(username='teste10', password='exemplo1234')
        self.assertEqual(resposta, True, msg='O usuario não foi criado e por isso não conseguiu fazer login')