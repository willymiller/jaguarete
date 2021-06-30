from django import forms
from django.forms.models import ModelForm
from apps.models import Producto, Categorias

class ProductoAltaForm(forms.ModelForm):
#    titulo = forms.CharField(label='Título', widget=forms.TextInput(attrs={'class': 'titulo'}), max_length=250, required=True, help_text='Requerido. Ingrese el nombre del producto.')
#    imagen = forms.FileInput(attrs={'name':'imagen', 'class': 'imagen'}),
#    contenido = forms.Textarea(attrs={'class': 'contenido'}),
#    precio = forms.IntegerField(),

#    class Meta:
#        model = Producto
#        fields = ('categoria', 'titulo', 'imagen', 'contenido', 'precio', )
    precio = forms.IntegerField(),
    class Meta:
        model = Producto
        fields = ('categoria', 'titulo', 'imagen', 'contenido', 'precio')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'titulo'}),
            'contenido': forms.Textarea(attrs={'class': 'contenido'}),
            'imagen': forms.FileInput(attrs={'name':'imagen', 'class': 'imagen'}),
        }
