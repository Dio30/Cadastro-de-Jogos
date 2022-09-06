from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

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
        if User.objects.filter(email=e).exists():
            raise ValidationError(f'O email {e} já existe.')
        return e