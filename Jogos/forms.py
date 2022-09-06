from django import forms
from .models import Jogos, Perfil
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

escolhas = [
    ('Ação', 'Ação'),
    ('Aventura', 'Aventura'),
    ('Futebol', 'Futebol'),
    ('RPG', 'RPG'),
    ('Outros', 'Outros'),
]

class JogosForm(forms.ModelForm):
    class Meta:
        model = Jogos
        fields = ('nome_do_jogo', 'estilo_do_jogo', 'imagem')
        widgets = {
            'nome_do_jogo': forms.TextInput(attrs={'spellcheck':'false', 'autofocus':'on', 'placeholder':'Insira o nome do jogo'}), #input
            'estilo_do_jogo': forms.RadioSelect(choices=escolhas)
        }
        
    def clean_nome_do_jogo(self):
        u = self.cleaned_data['nome_do_jogo']
        if Jogos.objects.filter(nome_do_jogo=u).exists():
            raise ValidationError("O jogo {} já existe.".format(u))
        return u
        
class PerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        
class PerfilUpdate(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['imagem_perfil',]
        