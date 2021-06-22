from demo.settings import TEMPLATES
from django.db import models
from django.db.models.fields import IntegerField
from django.contrib.auth.models import User

# Create your models here.

class componente(models.Model):
    idcomponente = models.AutoField(primary_key=True, verbose_name='Id de componente')
    nombrecomponente = models.CharField(max_length=99, verbose_name='Nombre de componente')

    def __str__(self):
        return  'Componente: ' + self.nombrecomponente

class fabricante(models.Model):
    idfabricante = models.AutoField(primary_key=True, verbose_name='Id de fabricante')
    nombrefabricante = models.CharField(max_length=99, verbose_name='Nombre de fabricante')

    def __str__(self):
        return  'Fabricante: ' + self.nombrefabricante

class producto(models.Model):
    idproducto = models.AutoField(primary_key=True, verbose_name='Id de producto')
    nombreproducto = models.CharField(max_length=99, verbose_name='Nombre de producto')
    fabricanteproducto = models.ForeignKey(fabricante, on_delete=models.CASCADE, verbose_name='Fabricante del producto')
    componenteproducto = models.ForeignKey(componente, on_delete=models.CASCADE, verbose_name='Componente de producto')
    precioproducto = models.IntegerField(default=0, verbose_name='Precio del producto')
    stockproducto = models.IntegerField(default=0, verbose_name='Stock del producto')
    imagenproducto = models.ImageField(null=True, blank=True, upload_to ='img', verbose_name='Imagen del producto')

    def __str__(self):
        return  'Producto: ' + self.nombreproducto

class cuenta(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        get_username = User
        return 'Usuario: ' + self.get_username()


