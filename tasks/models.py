from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class task(models.Model):
    Equipo= models.CharField(max_length=200)
    Cantidad= models.CharField(max_length=200)
    Serial=models.CharField(max_length=200)
    Bien_Nacional=models.CharField(max_length=200)
    Nota =models.TextField(blank=True) 
    Creado= models.DateTimeField(auto_now_add=True)
    Fecha_entrega =models.DateTimeField(blank=True, null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Equipo + ' by-' +self.user.username 
    