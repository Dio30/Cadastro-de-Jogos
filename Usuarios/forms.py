from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuariosForm(UserCreationForm):
    email = forms.EmailField(min_length=11, required=False)
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            'username': forms.TextInput(attrs={'class':'text-muted'})
        }
        