from django.db import models
from django.contrib.auth.models import User

class Receta(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    nombre_receta = models.CharField(max_length=100)
    descripcion_receta = models.TextField()
    imagen_receta = models.ImageField(upload_to="recetas", null=True, blank=True)
    ver_contar_receta = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nombre_receta

