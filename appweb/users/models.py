from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    imagen = models.ImageField(upload_to="avatares", blank=True, null=True)
    
    def __str__(self):
        return f"{self.user} - {self.imagen}"
    