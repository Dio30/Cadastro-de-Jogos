from django import forms
from .models import Jogos
from django.core.exceptions import ValidationError

class JogosForm(forms.ModelForm):
    class Meta:
        model = Jogos
        fields = ('nome_do_jogo', 'estilo_do_jogo', 'imagem')
        widgets = {
            'nome_do_jogo': forms.TextInput
            (attrs={'spellcheck':'false', 'autofocus':'on', 'placeholder':'Nome do jogo', 
                    'id':'inputUser', 'class':'form-control', 'autocapitalize': 'off'}), #input
            
            'estilo_do_jogo': forms.RadioSelect,
        }
    
    #def clean_nome_do_jogo(self):
    #    j = self.cleaned_data['nome_do_jogo']
    #    jogo = Jogos.objects.filter(nome_do_jogo=j)
    #    if jogo.exists():
    #        raise ValidationError(f'O jogo {j} já existe.')
    #    return j