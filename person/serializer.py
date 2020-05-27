from .models import Person, TipoDocumento, Ciudad
from rest_framework import serializers

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id','tipoDocumento', 'numeroDocumento', 'nombre', 'apellido','ciudad']

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = '__all__'

class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = '__all__'
