from django.shortcuts import render, redirect, get_object_or_404
from .models import Receta


def recetas(request):
    if request.method == 'POST':
        datos = request.POST
        nombre_receta = datos.get('nombre_receta')
        descripcion_receta = datos.get('descripcion_receta')
        imagen_receta = request.FILES.get('imagen_receta')
        Receta.objects.create(
            nombre_receta=nombre_receta,
            descripcion_receta=descripcion_receta,
            imagen_receta=imagen_receta
        )
        return redirect('/')
    las_recetas=Receta.objects.all()
    if request.GET.get('buscar'):
        las_recetas=las_recetas.filter(nombre_receta__icontains=request.GET.get('buscar'))
    diccionario = {'las_recetas': las_recetas}
    return render(request, 'receta.html', diccionario)

def borrar_receta(request, id):
    receta = get_object_or_404(Receta, id=id)
    receta.delete()
    return redirect('/')

def actualizar_receta(request, id):
    receta = Receta.objects.get(id=id)

    if request.method == 'POST':
        receta.nombre_receta = request.POST.get('nombre_receta')
        receta.descripcion_receta = request.POST.get('recipe_description')
        
        if request.FILES.get('imagen_receta'):
            receta.imagen_receta = request.FILES['imagen_receta']
        
        receta.save()
        return redirect('/')  # o a donde necesites

    return render(request, 'actualizar_receta.html', {'receta': receta})



















