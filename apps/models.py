from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your models here.
class Categorias(models.Model):
    categoria = models.CharField(max_length=64, null=False)

    def __str__(self):
        return f"{self.categoria}"

class Producto(models.Model):
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, related_name="clasificacion_categoria")
    titulo = models.CharField(max_length=250, null=False)
    imagen = models.FileField(upload_to='imagenes/')
    contenido = models.CharField(max_length=2000, null=False)
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.titulo} {self.imagen} {self.descripcion} {self.precio} "

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario")
    producto = models.ManyToManyField(Producto)

    #def __str__(self):
    #    return HttpResponse("agregado")
    #    return f"{self.usuario} - {self.producto}"