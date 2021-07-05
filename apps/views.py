from django.db.models import query
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from apps.forms import *
from django.db.models import Q
from apps.models import Producto, Categorias, Carrito
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, "index.html", {
            "lista_categorias": Categorias.objects.all(),
            "lista_productos_principales": Producto.objects.all()[:3],
            "lista_productos": Producto.objects.all()[3:100], 
        })

def contacto(request):
    return render(request, "contacto.html", {
        "lista_categorias": Categorias.objects.all(),
        "lista_productos_principales": Producto.objects.all()[:3],
        "lista_productos": Producto.objects.all()[3:100],
    })

def acercade(request):
    return render(request, "acercade.html", {
        "lista_categorias": Categorias.objects.all(),
        "lista_productos_principales": Producto.objects.all()[:3],
        "lista_productos": Producto.objects.all()[3:100],
    })

@login_required
def producto_alta(request):
    if request.method == 'POST':
        form = ProductoAltaForm(request.POST, request.FILES, instance=Producto(imagen=request.FILES['imagen']))
        if form.is_valid():
            form.save()          
            return HttpResponseRedirect(reverse('producto_alta'))
    else:
        form = ProductoAltaForm()
    return render(request, 'producto_alta.html', {
        'form': form
        })

@login_required
def producto_editar(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    form = ProductoAltaForm(request.POST or None,instance=producto)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        return render(request, 'producto_editar.html', {'form': form})

#def producto_editar(request, producto_id):
#    un_producto = get_object_or_404(Producto, id=producto_id)
#    return render(request, "producto_editar.html", {
#        "producto": un_producto
#    })

def producto(request, producto_id):
    un_producto = get_object_or_404(Producto, id=producto_id)
    return render(request, "producto.html", {
        "producto": un_producto
    })

def filtro_categorias(request, categoria_id):
    una_categoria = get_object_or_404(Categorias, id=categoria_id)
    queryset = Producto.objects.all()
    queryset = queryset.filter(categoria=una_categoria)
    return render(request,"index.html", {
        "lista_productos": queryset,
        "lista_categorias": Categorias.objects.all(),
        "categoria_seleccionada": una_categoria
    })

@login_required
def agregar_al_carrito(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    carrito = Carrito.objects.get_or_create(usuario_id=request.user.id)[0]
    carrito.usuario = User.objects.get(id=request.user.id)
    carrito.producto.add(producto)
    carrito.save()
    return redirect("carrito")

@login_required
def carrito(request):
    carrito = Carrito.objects.get_or_create(usuario=request.user)[0]
    precio_total = 0.00
    for item in carrito.producto.all():
        precio_total += item.precio
    return render(request, "carrito.html", {"productos": carrito.producto, "precio_total": precio_total})

@login_required
def borrar_carrito(request):
    carrito = Carrito.objects.get(usuario=request.user)
    for producto in carrito.producto.all():
        carrito.producto.remove(producto)
    return redirect("carrito")

def buscar(request):
    queryset = request.GET.get("buscar")
    return render(request, "index.html", { 
            "lista_busqueda": Producto.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(contenido__icontains = queryset)).distinct()
        })

def borrar_item_carrito(request, producto_id):
    carrito = Carrito.objects.get(usuario=request.user)
    producto = carrito.producto.get(id=producto_id)
    carrito.producto.remove(producto)
    return redirect("carrito")
