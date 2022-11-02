from django.urls import path
from .views import UsuariosViews, PerfilUpdateView, ChangePasswordView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cadastro/', UsuariosViews.as_view(), name='cadastrar'),
    path('', auth_views.LoginView.as_view(template_name='cadastro/login.html'), name='login'),
    path('sair/', auth_views.LogoutView.as_view(), name='logout'),
    path('perfil_edit/', PerfilUpdateView.as_view(), name='perfil_edit'),
    path('trocar_senha/', ChangePasswordView.as_view(), name='trocar_senha'),
    path('senha_reset/', auth_views.PasswordResetView.as_view(template_name="cadastro/senha_reset.html"), name='senha_reset'),
    path('senha_reset_email/', auth_views.PasswordResetDoneView.as_view(template_name="cadastro/senha_reset_email.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="cadastro/senha_reset_confirm_view.html"), name='password_reset_confirm'),
    path('senha_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="cadastro/senha_reset_complete.html"), name='password_reset_complete'),
]