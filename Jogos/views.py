from .forms import JogosForm
from .models import Jogos
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class JogosList(LoginRequiredMixin, ListView):
    model = Jogos
    template_name = 'jogos/jogos_list.html'
    queryset = Jogos.objects.order_by('nome_do_jogo').all()
    login_url = reverse_lazy('login')
    paginate_by = 3
    
    def get_queryset(self): # para cada usuario ser unico e não ter acesso a qualquer coisa de outros usuarios cadastrados
        self.object_list = Jogos.objects.filter(usuario=self.request.user)
        return self.object_list
    
class JogosDetail(LoginRequiredMixin, DetailView):
    queryset = Jogos.objects.all()
    login_url = reverse_lazy('login')
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Jogos, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object
    
class JogosNew(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = JogosForm
    template_name = 'jogos/jogos_form.html'
    success_message = 'Jogo adicionado com sucesso!'
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
    success_message = 'Jogo editado com sucesso!'
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
    success_message = 'Jogo deletado com sucesso!'
    login_url = reverse_lazy('login')
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Jogos, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object