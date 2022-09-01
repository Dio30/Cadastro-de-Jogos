from django import forms
from .models import Jogos, Perfil
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

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
        
class PerfilForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'