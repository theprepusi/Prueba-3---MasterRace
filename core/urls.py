from django.contrib import admin
from django.urls import path, include
from core.views import  home, login

urlpatterns = [
    path('', home, name='home'),
    path('login', login, name='login'),
]