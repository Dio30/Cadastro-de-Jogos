from django.urls import path
from .views import UsuariosViews
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cadastro/', UsuariosViews.as_view(), name='cadastrar'),
    path('', auth_views.LoginView.as_view(template_name='cadastro/login.html'), name='login'),
    path('sair/', auth_views.LogoutView.as_view(), name='logout'),
]