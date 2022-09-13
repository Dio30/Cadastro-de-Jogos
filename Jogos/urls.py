from django.urls import path
from .views import JogosList, JogosNew, JogosEdit, JogosDelete, JogosDetail

urlpatterns = [
    path('lista/', JogosList.as_view(), name='lista_jogos'),
    path('novo_jogo/', JogosNew.as_view(), name='novo'),
    path('imagem/<int:pk>/', JogosDetail.as_view(), name='imagem'),
    path('editar_jogo/<int:pk>/', JogosEdit.as_view(), name='editar'),
    path('deletar/<int:pk>/', JogosDelete.as_view(), name='deletar'),
]