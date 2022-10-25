from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.JogosList.as_view(), name='lista_jogos'),
    path('novo_jogo/', views.JogosNew.as_view(), name='novo'),
    path('imagem/<int:pk>/', views.JogosDetail.as_view(), name='imagem'),
    path('editar_jogo/<int:pk>/', views.JogosEdit.as_view(), name='editar'),
    path('deletar/<int:pk>/', views.JogosDelete.as_view(), name='deletar'),
]