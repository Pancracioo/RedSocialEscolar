from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

class Usuarios(AbstractUser):
    #user id
    profile = models.URLField()
    # gradeId
    # classId
    username = models.CharField(null=False, max_length= 55)
    password = models.CharField(null=False, max_length= 55)
    email = models.CharField(null=True, max_length= 55)
    tel = models.CharField(null=True, max_length= 20)
    date_birtch = models.DateField(null=True)
    date_reg = models.DateField(default=timezone.now)
    #permison
    def __str__(self):
        return f"{self.username}"
    def delete(self, *args, **kwargs):
        self.profile.delete()
        super().delete(*args, **kwargs)
