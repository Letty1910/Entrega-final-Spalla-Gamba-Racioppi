from django.db import models

class Cliente(models.Model):
    nombre_completo = models.CharField(max_length=100)
    cuit = models.CharField(max_length=11)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    localidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_completo

class Tractor(models.Model):
    familia = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    serie = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.familia} {self.modelo}"

class Cosechadora(models.Model):
    familia = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    serie = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.familia} {self.modelo}"