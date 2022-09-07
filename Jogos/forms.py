from django import forms
from .models import Jogos

class JogosForm(forms.ModelForm):
    class Meta:
        model = Jogos
        fields = ('nome_do_jogo', 'estilo_do_jogo', 'imagem')
        widgets = {
            'nome_do_jogo': forms.TextInput(attrs={'spellcheck':'false', 'autofocus':'on', 'placeholder':'Insira o nome do jogo'}), #input
            'estilo_do_jogo': forms.RadioSelect
        }