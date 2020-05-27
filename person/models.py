from django.db import models

class TipoDocumento(models.Model):
    tipo_Documento = models.CharField(max_length=4, unique=True)

class Ciudad(models.Model):
    nombre_Ciudad = models.CharField(max_length=50, unique=True)

# Create your models here.
class Person(models.Model):
    tipoDocumento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    #tipoDocumento = models.CharField(max_length=4)
    numeroDocumento = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    #ciudad = models.CharField(max_length=50)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
