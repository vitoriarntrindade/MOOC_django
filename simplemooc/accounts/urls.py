from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path("entrar/", auth_views.LoginView.as_view(template_name='accounts/login.html'), name="login"),
]
