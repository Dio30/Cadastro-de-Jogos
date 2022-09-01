from .forms import JogosForm, PerfilForm
from .models import Jogos, Perfil
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

class JogosList(LoginRequiredMixin, ListView):
    model = Jogos
    template_name = 'jogos/jogos_list.html'
    queryset = Jogos.objects.order_by('nome_do_jogo').all
    login_url = reverse_lazy('login')
    
    def get_queryset(self): # para cada usuario ser unico e não ter acesso a qualquer coisa de outros usuarios cadastrados
        self.object_list = Jogos.objects.filter(usuario=self.request.user)
        return self.object_list
    
    def get(self, request, *args, **kwargs):
        pesquisar = self.request.GET.get('nome_do_jogo')
        if pesquisar:
            self.object_list = self.get_queryset().filter(nome_do_jogo__icontains=pesquisar)
        else:
            self.object_list = self.get_queryset
        
        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)
    
class JogosDetail(LoginRequiredMixin, DetailView):
    queryset = Jogos.objects.all()
    login_url = reverse_lazy('login')
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Jogos, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object
    
class JogosNew(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = JogosForm
    template_name = 'jogos/jogos_form.html'
    success_message = 'Jogo adicionado com sucesso'
    success_url = reverse_lazy('lista_jogos')
    login_url = reverse_lazy('login')
    
    def form_valid(self, form): # para validar o formulario
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url
    
    def get_context_data(self, *args ,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastro de Jogos'
        context['botao'] = 'Cadastrar'
        return context
    
class JogosEdit(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = JogosForm
    template_name = 'jogos/jogos_form.html'
    success_message = 'Jogo editado com sucesso'
    success_url = reverse_lazy('lista_jogos')
    login_url = reverse_lazy('login')
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Jogos, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object
    
    def get_context_data(self, *args ,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Editar'
        context['botao'] = 'Editar'
        return context
    
class JogosDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    queryset = Jogos.objects.all()
    success_url = reverse_lazy('lista_jogos')
    success_message = 'Jogo deletado com sucesso'
    login_url = reverse_lazy('login')
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Jogos, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object
    
###############################################################################################################################
@login_required(login_url ='login')

def perfil(request):
    if request.method == "GET":
        return render(request, 'cadastro/perfil.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        usuario = User.objects.filter(username=username).exclude(id=request.user.id)
        form = PerfilForm(data=request.POST, files=request.FILES)
        
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request, 'cadastro/perfil.html', {'obj': obj})
        
        if usuario.exists():
            messages.error(request, f"Já existe um usuario com esse nome: {username}")
            return render(request, 'cadastro/perfil.html')
        
        meu_email = User.objects.filter(email=email).exclude(id=request.user.id)
        
        if meu_email.exists():
            messages.error(request, f"Já existe um usuario com esse email: {email}")
            return render(request, 'cadastro/perfil.html')
        
        request.user.username = username
        request.user.email = email
        request.user.save()
        messages.success(request, "Dados alterados com sucesso")
        
    else:
        form = PerfilForm()
    img = Perfil.objects.all()
    return render(request, 'cadastro/perfil.html', {'form':form, 'img':img})
