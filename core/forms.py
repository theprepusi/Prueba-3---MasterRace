from django import forms
from django.forms import ModelForm
from .models import cuenta

class CuentaForm(ModelForm):

    class Meta:
        model = cuenta
        fields =['usuario', 'password']