from django.conf import settings
from .forms import JogosForm
from .models import Jogos
from .pagination import MyPaginator
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.auth.models import User

class JogosList(LoginRequiredMixin, ListView):
    model = Jogos
    template_name = 'jogos/jogos_list.html'
    login_url = reverse_lazy('login')
    paginator_class = MyPaginator
    paginate_by = 3
    
    def get_queryset(self): # para cada usuario ser unico e não ter acesso a qualquer coisa de outros usuarios cadastrados
        user = self.request.user
        if user.is_superuser:
            self.object_list = Jogos.objects.all()
        else:
            self.object_list = Jogos.objects.filter(usuario=self.request.user)
        return self.object_list
    
    def get(self, request, *args, **kwargs): #para pesquisar pelo nome do carro
        pesquisar = self.request.GET.get('nome_do_jogo')
        if pesquisar:
            self.object_list = self.get_queryset().filter(nome_do_jogo__icontains=pesquisar)
        else:
            self.object_list = self.get_queryset()
            
        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)
    
class JogosDetail(LoginRequiredMixin, DetailView):
    queryset = Jogos.objects.all()
    login_url = reverse_lazy('login')
    
    def get_object(self, queryset=None):
        user = self.request.user
        if user.is_superuser:
            self.object = get_object_or_404(Jogos, pk=self.kwargs['pk'])
        else:
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
        user = self.request.user
        if user.is_superuser:
            self.object = get_object_or_404(Jogos, pk=self.kwargs['pk'])
        else:
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
        user = self.request.user
        if user.is_superuser:
            self.object = get_object_or_404(Jogos, pk=self.kwargs['pk'])
        else:
            self.object = get_object_or_404(Jogos, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

def enviar_email(request):
    if request.method == 'POST':
        assunto = request.POST.get('assunto')
        mensagem = request.POST.get('mensagem')
        email = request.POST.get('email')
        enviar=EmailMessage(subject=assunto, body=mensagem, from_email=settings.DEFAULT_FROM_EMAIL, 
                            to=[settings.DEFAULT_FROM_EMAIL], reply_to=[email])
        enviar.send(fail_silently=False)
        messages.success(request, "Email enviado com sucesso, muito obrigado pelo contato!")
        context = {
            "assunto":assunto,
            "mensagem":mensagem,
            "email":email,
        }
        return render(request, "jogos/enviar_email.html", context)
    
    else:
        return render(request, "jogos/enviar_email.html")