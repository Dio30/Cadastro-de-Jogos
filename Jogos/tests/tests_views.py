from django.test import TestCase
from django.urls import reverse

class JogosListViewTest(TestCase):
    def test_status_code_200(self):
        resposta = self.client.get(reverse('lista_jogos'))
        self.assertEquals(resposta.status_code, 200)
        
    def test_template_usado(self):
        resposta = self.client.get(reverse('lista_jogos'))
        self.assertTemplateUsed(resposta, 'jogos/jogos_list.html')

class JogosNovoViewsTest(TestCase):
    def test_status_code_200(self):
        resposta = self.client.get(reverse('novo'))
        self.assertEquals(resposta.status_code, 200)
        
    def test_template_usado(self):
        resposta = self.client.get(reverse('novo'))
        self.assertTemplateUsed(resposta, 'jogos/jogos_form.html')