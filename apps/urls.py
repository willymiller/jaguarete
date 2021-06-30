from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('contacto', views.contacto, name="contacto"),
    path('acercade', views.acercade, name="acercade"),
    path('carrito', views.carrito, name="carrito"),
    path('producto_alta', views.producto_alta, name="producto_alta"),
    path('agregar_al_carrito/<int:producto_id>', views.agregar_al_carrito, name="agregar_al_carrito"),
    path('filtro_categorias/<int:categoria_id>', views.filtro_categorias, name="filtro_categorias"),
    path('<int:producto_id>', views.producto, name="producto"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)