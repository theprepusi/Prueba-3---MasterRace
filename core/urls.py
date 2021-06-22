from django.contrib import admin
from django.urls import path, include
from core.views import  cpu, gpu, hdd, home, login, m2, mb, psu, ram, signup, ssd, form_cuenta

urlpatterns = [
    path('', home, name='home'),
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('cpu', cpu, name='cpu'),
    path('gpu', gpu, name='gpu'),
    path('hdd', hdd, name='hdd'),
    path('m2', m2, name='m2'),
    path('mb', mb, name='mb'),
    path('psu', psu, name='psu'),
    path('ram', ram, name='ram'),
    path('ssd', ssd, name='ssd'),
    path('form-cuenta', form_cuenta, name="form_cuenta"),   
]