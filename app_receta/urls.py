from django.urls import path
from . import views

urlpatterns = [
    path('', views.recetas, name='recetas'),
    path('borrar_receta/<int:id>', views.borrar_receta, name='borrar_receta'),
    path('actualizar_receta/<int:id>', views.actualizar_receta, name='actualizar_receta'),
]