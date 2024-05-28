from django.urls import path, include
from core import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact")

]