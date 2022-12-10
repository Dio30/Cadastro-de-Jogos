from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Perfil

class UsuariosForm(UserCreationForm):
    email = forms.EmailField(required=False)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
    def clean_username(self):
        u = self.cleaned_data['username']
        user = User.objects.filter(username=u)
        if user.exists():
            raise ValidationError(f'O usuário {u} já existe.')
        
        if u.isnumeric():
            raise ValidationError('O usuário não pode ser somente numérico.')
        return u
    
    def clean_email(self):
        e = self.cleaned_data['email']
        email = User.objects.filter(email=e).exclude(email='')
        if email.exists():
            raise ValidationError(f'O email {e} já existe.')
        return e
    
class PerfilUpdate(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'
        exclude = ['usuario',]
        
class PerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput
            (attrs={'spellcheck':'false', 'id':'inputUser', 'class':'form-control', 
                    'placeholder':'Usuário', 'autocapitalize': 'off'}), #input
            
            'email': forms.EmailInput(attrs={'spellcheck':'false', 'placeholder':'Email', 
                                     'id':'inputUser', 'class':'form-control', 'autocapitalize': 'off'}) #input
            }
        
    # para poder trocar o nome do usuário excluindo ele mesmo, se não aparecerá um erro
    def clean_username(self):
        u = self.cleaned_data['username']
        user = User.objects.filter(username=u).exclude(id=self.instance.id) 
        if u.isnumeric():
            raise ValidationError('O usuário não pode ser somente numérico.')
        if user.exists():
            raise ValidationError(f'O usuário {u} já existe!')
        return u
    
    def clean_email(self):
        e = self.cleaned_data['email']
        email = User.objects.filter(email=e).exclude(id=self.instance.id).exclude(email='')
        if email.exists():
            raise ValidationError(f'O email {e} já existe!')
        return e

class PasswordForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput
                (attrs={'class':'form-control', 'placeholder':'Senha Atual', 'spellcheck':'false', 'autofocus':'on', 'id':'senha'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput
                (attrs={'class':'form-control', 'placeholder':'Nova Senha', 'id':'senha2'}))
    new_password2 =  forms.CharField(max_length=100, widget=forms.PasswordInput
                (attrs={'class':'form-control', 'placeholder':'Nova Senha', 'id':'senha3'}))
    
    class Meta:
        model = User
        fields = ("old_password", "new_password1", "new_password2")

class PasswordReset(PasswordResetForm):
    email = forms.EmailField(max_length=100,
        widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email', 
                                       'autofocus':'on', 'spellcheck':'false'}),
    )
    
    def clean_email(self):
        e_mail = self.cleaned_data['email']
        user = User.objects.filter(email=e_mail)
        if not user.exists(): # se o email não existir no banco de dados
            raise ValidationError("Esse email não está cadastrado.")
        return e_mail