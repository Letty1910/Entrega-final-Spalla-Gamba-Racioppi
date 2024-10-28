from django.db import models
from django.contrib.auth.models import User

class MaquinaAgricola(models.Model):
    Maquina_Seleccion = [
        ('Tractores', 'Tractores'),
        ('Cosechadoras', 'Cosechadoras'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    maquina = models.CharField(max_length=15, choices=Maquina_Seleccion, default='Tractores')
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    descripcion = models.TextField(null=True, blank=True)
    year = models.IntegerField() 
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    telefonoContacto = models.IntegerField()
    emailContacto = models.EmailField()
    imagenMaquina = models.ImageField(null=True, blank=True, upload_to="imagenes/")

    class Meta:
        ordering = ['usuario', '-fechaPublicacion']

    def _str_(self):
        return self.titulo    

class Comentario(models.Model):
    comentario = models.ForeignKey(MaquinaAgricola, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def _str_(self):
        return '%s - %s' % (self.nombre, self.comentario)
    