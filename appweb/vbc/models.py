from django.db import models

# Create your models here.

class ServicioList(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    valoracion = models.PositiveSmallIntegerField()

def __str__(self):
    texto = "{0} ({1})"
    return texto.format(self.nombre, self.valoracion)