from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from apps.forms import *
from .forms import *
from django.contrib.auth import login

def registrarse(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("index")
            #form.save()          
            #return render(request, 'registration/login.html', {
        #"lista_categorias": Categorias.objects.all(),
        #})
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {
        'form': form,
        "lista_categorias": Categorias.objects.all(),
        })
