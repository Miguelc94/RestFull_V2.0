from rest_framework import routers

from .viewsets import PersonViewSet, TipoDocumentoViewSet, CiudadViewSet

router = routers.SimpleRouter()
router.register('persons', PersonViewSet)
router.register('tipoDocumento', TipoDocumentoViewSet)
router.register('nombreCiudad', CiudadViewSet)

urlpatterns = router.urls
