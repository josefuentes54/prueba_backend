from django.db import models

class Libros(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    añoLanzamiento = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
