from rest_framework import serializers
from .models import Libros

class LibrosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Libros
        fields = ('id', 'titulo', 'autor', 'añoLanzamiento', 'descripcion')