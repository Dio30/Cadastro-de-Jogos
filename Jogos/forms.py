from django import forms
from .models import Jogos

class JogosForm(forms.ModelForm):
    class Meta:
        model = Jogos
        fields = ('nome_do_jogo', 'estilo_do_jogo', 'imagem')
        widgets = {
            'nome_do_jogo': forms.TextInput(attrs={'spellcheck':'false', 'autofocus':'on', 'placeholder':'Nome do jogo', 
                    'id':'inputUser', 'class':'form-control', 'autocapitalize': 'off'}), #input
            
            'estilo_do_jogo': forms.RadioSelect,
        }