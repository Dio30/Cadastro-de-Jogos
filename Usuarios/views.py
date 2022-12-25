from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import PasswordForm, PerfilForm, PerfilUpdate, UsuariosForm, PasswordReset
    
class UsuariosViews(SuccessMessageMixin, CreateView):
    template_name = 'cadastro/cadastrar.html'
    form_class = UsuariosForm
    success_message = "Usuário criado com sucesso"
    success_url = reverse_lazy('login')

class PerfilUpdateView(LoginRequiredMixin, TemplateView):
    template_name = 'cadastro/perfil_edit.html'

    def post(self, request, username):
        profile = request.user.perfil
        form = PerfilForm(request.POST or None, instance=request.user)
        perfil = PerfilUpdate(data=request.POST, files=request.FILES, instance=profile)
      
        if form.is_valid() and perfil.is_valid():
            form.save()
            perfil.save()
            messages.success(request, "Dados alterados com sucesso!")
            return HttpResponseRedirect(reverse_lazy('lista_jogos'))
        
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
    
class PasswordReset(PasswordResetView):
    template_name= "cadastro/senha_reset.html"
    form_class = PasswordReset