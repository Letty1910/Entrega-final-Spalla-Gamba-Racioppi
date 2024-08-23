from django.db import models
    
class cliente(models.Model):
    nombre_completo = models.CharField(max_length=50)
    cuit = models.IntegerField()
    email = models.EmailField()
    localidad = models.CharField(max_length=50)

class tractores(models.Model):
    familia = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    serie = models.CharField(max_length=30)

class cosechadoras(models.Model):
    familia = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    serie = models.CharField(max_length=30)

class ventas(models.Model):
    cuit = models.IntegerField()
    fecha_de_venta = models.DateField()
    entregado = models.BooleanField()  