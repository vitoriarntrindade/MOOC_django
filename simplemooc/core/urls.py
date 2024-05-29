from django.urls import path, include
from core import views

app_name = 'core'


urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact")

]