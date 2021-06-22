from core.forms import CuentaForm
from django.shortcuts import render
from .models import producto

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def login(request):
    return render(request, 'login.html', {})

def signup(request):
    return render(request, 'signup.html', {})

def cpu(request):
    return render(request, 'cpu.html', {})

def gpu(request):
    return render(request, 'gpu.html', {})

def hdd(request):
    return render(request, 'hdd.html', {})

def m2(request):
    return render(request, 'm2.html', {})

def mb(request):
    return render(request, 'mb.html', {})

def psu(request):
    return render(request, 'psu.html', {})

def ram(request):
    return render(request, 'ram.html', {})
    
def ssd(request):
    return render(request, 'ssd.html', {})

def home(request):
    productos = producto.objects.all()
    datos = {
        'productos': productos
    }
    return render(request, 'home.html', datos)

def form_cuenta(request):
    datos = {
        'formi': CuentaForm()
    }

    if request.method == 'POST':

        formulario = CuentaForm(request.POST)

        if formulario.is_valid:

            formulario.save()

            datos['mensaje'] = "Logeo éxitoso"

    return render(request, 'login.html', datos)