from django.contrib import admin
from .models import Categorias, Carrito, Producto

# Register your models here.
admin.site.register(Categorias)
admin.site.register(Carrito)
admin.site.register(Producto)