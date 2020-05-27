from rest_framework import viewsets
from .models import Person, TipoDocumento, Ciudad
from .serializer import PersonSerializer, TipoDocumentoSerializer, CiudadSerializer

class CiudadViewSet(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer

class TipoDocumentoViewSet(viewsets.ModelViewSet):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
