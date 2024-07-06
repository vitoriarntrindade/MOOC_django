from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from .views import register

app_name = 'accounts'

urlpatterns = [
    path("entrar/", LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path("cadastro/", register, name="register"),
    path("sair/", LogoutView.as_view(next_page='/'), name="logout")
]
