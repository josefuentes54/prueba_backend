from .models import Libros
from rest_framework import viewsets, permissions
from .serializers import LibrosSerializers

class LibrosSerializersViewSet(viewsets.ModelViewSet):
    queryset = Libros.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LibrosSerializers