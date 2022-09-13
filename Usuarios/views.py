from .forms import UsuariosForm, PerfilForm, PerfilUpdate, PasswordForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView

class UsuariosViews(SuccessMessageMixin, CreateView):
    template_name = 'cadastro/cadastrar.html'
    form_class = UsuariosForm
    success_message = "Usuário criado com sucesso"
    success_url = reverse_lazy('login')
    
class PerfilList(LoginRequiredMixin, TemplateView):
    template_name = 'cadastro/perfil.html'

class PerfilUpdateView(LoginRequiredMixin, TemplateView):
    template_name = 'cadastro/perfil_edit.html'

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        profile = request.user.perfil
        form = PerfilForm(request.POST or None, instance=request.user)
        perfil = PerfilUpdate(data=request.POST, files=request.FILES, instance=profile)
        usuario = User.objects.filter(username=username).exclude(id=request.user.id)
        
        if usuario.exists():
            messages.error(request, f"Já existe um usuario com esse nome: {username}")
            return HttpResponseRedirect(reverse_lazy('perfil_edit'))
        
        meu_email = User.objects.filter(email=email).exclude(id=request.user.id)
        
        if meu_email.exclude(email='').exists():
            messages.error(request, f"Já existe um usuario com esse email: {email}")
            return HttpResponseRedirect(reverse_lazy('perfil_edit'))
        
        if form.is_valid() and perfil.is_valid():
            form.save()
            perfil.save()
            messages.success(request, "Dados alterados com sucesso")
            return HttpResponseRedirect(reverse_lazy('perfil'))
        
        context = self.get_context_data(perfil=perfil, form=form)
        return self.render_to_response(context)
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
class ChangePasswordView(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView): #caso queria alterar a sua senha
    form_class = PasswordForm
    template_name = 'cadastro/trocar_senha.html'
    success_message = "Senha alterada com sucesso"
    success_url = reverse_lazy('lista_jogos')
    login_url = reverse_lazy('login') # se alguem tentar entrar em alguma pagina sem estar autenticado será redirecionado para o login