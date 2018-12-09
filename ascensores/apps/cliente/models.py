from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    direccion= models.CharField(max_length=50,blank=False)
    ciudad= models.CharField(max_length=50, blank=False)
    comuna =models.CharField(max_length=50,blank=False)
    correo= models.CharField(max_length=50, blank=True)
    telefono = models.CharField(max_length=50,blank=True)


    def __str__(self):
        return super().__str__()