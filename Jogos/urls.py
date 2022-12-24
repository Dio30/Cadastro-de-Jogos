from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.JogosList.as_view(), name='lista_jogos'),
    path('novo_jogo/', views.JogosNew.as_view(), name='novo'),
    path('imagem/<slug:slug>/', views.JogosDetail.as_view(), name='imagem'),
    path('editar_jogo/<slug:slug>/', views.JogosEdit.as_view(), name='editar'),
    path('deletar/<slug:slug>/', views.JogosDelete.as_view(), name='deletar'),
    path('enviar_email', views.enviar_email, name='enviar_email')
]