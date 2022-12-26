from rest_framework import routers
from .api import LibrosSerializersViewSet

router = routers.DefaultRouter()
router.register('api/libros', LibrosSerializersViewSet, 'libros')

urlpatterns = router.urls