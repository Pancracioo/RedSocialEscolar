from django.db import models

# Create your models here.


#Sin migraciones
class EscuelaMainConfig(models.Model):

    nombre = models.CharField(max_length=100, null=False)
    eslogan = models.CharField(max_length=200, null=True)
    direccion = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    telefono = models.CharField(max_length=25, null=True)
    logo = models.ImageField(upload_to='Settings/Images', null=True, blank=True)
    def __str__(self):
        return self.nombre
    def delete(self, *args, **kwargs):
        self.logo.delete()
        super().delete(*args, **kwargs)

class Usuarios(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    apellido = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False, unique=True)
    telefono = models.CharField(max_length=20, null=True)
    fecha_nac = models.DateField(null=True)
    permisos = models.Choices("estudiante", "profesor", "staff", "administrador")
    foto_perfil = models.ImageField(upload_to='Users/Images', null=True)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    def delete(self, *args, **kwargs):
        self.foto_perfil.delete()
        super().delete(*args, **kwargs)


