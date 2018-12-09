from django.db import models

# Create your models here.
class Usuario(models.Model):
    TIPO_USUARIO =(('tecnico','Tecnico'),('administrador','Administrador'))
    nombre_completo = models.CharField(max_length =80,blank = False)
    correo = models.EmailField(max_length = 120,blank = False)
    contraseña = models.CharField(max_length = 100, blank=False)
    tipo_usuario = models.CharField(max_length = 50,choices = TIPO_USUARIO,default = 'tipo usuario')

    def __str__(self):
        return self.nombre_completo
