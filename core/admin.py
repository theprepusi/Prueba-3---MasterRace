from core.models import componente, cuenta, fabricante, producto
from django.contrib import admin

# Register your models here.

admin.site.register(componente)
admin.site.register(fabricante)
admin.site.register(producto)
admin.site.register(cuenta)
