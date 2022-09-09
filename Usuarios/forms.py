from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Perfil

class UsuariosForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
    def clean_username(self):
        u = self.cleaned_data['username']
        if User.objects.filter(username=u).exists():
            raise ValidationError(f'O usuário {u} já existe.')
        return u
    
    def clean_email(self):
        e = self.cleaned_data['email']
        if User.objects.filter(email=e).exclude(email='').exists():
            raise ValidationError(f'O email {e} já existe.')
        return e
    
class PerfilUpdate(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'
        exclude = ['usuario',]
        
class PerfilForm(forms.ModelForm):
    email = forms.EmailField(help_text='Insira um email valido.', required=False, widget=forms.EmailInput
                             (attrs={'spellcheck':'false', 'placeholder':'Email', 'id':'inputUser', 'class':'form-control'})) #input
    class Meta:
        model = User
        fields = ['username', 'email',]
        widgets = {
            'username': forms.TextInput
            (attrs={'spellcheck':'false', 'autofocus':'on', 'id':'inputUser', 'class':'form-control', 'placeholder':'Usuário'}), #input
            }