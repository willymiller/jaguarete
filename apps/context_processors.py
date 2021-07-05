from apps.models import Categorias

def menu_categoria(request):
    categorias = Categorias.objects.all()
    return ({"categorias": categorias})