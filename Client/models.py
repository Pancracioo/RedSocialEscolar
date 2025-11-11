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


