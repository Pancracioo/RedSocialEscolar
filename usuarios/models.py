from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuarios(AbstractUser):
    nombre = models.CharField(max_length=100, null=False)
    apellido = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False, unique=True)
    telefono = models.CharField(max_length=20, null=True)
    fecha_nac = models.DateField(null=True)
    permisos = models.Choices("estudiante", "profesor", "staff", "administrador", default="estudiante")
    foto_perfil = models.ImageField(upload_to='Users/Images', null=True)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    def delete(self, *args, **kwargs):
        self.foto_perfil.delete()
        super().delete(*args, **kwargs)
