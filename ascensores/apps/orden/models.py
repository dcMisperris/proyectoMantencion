from django.db import models
from apps.cliente.models import Cliente
from apps.login.models import Usuario

# Create your models here.

class Orden(models.Model):
	"""docstring for Orden"""
	nro_folio=models.IntegerField(primary_key=True)
	fecha= models.DateField(blank= False)
	id_ascensor=models.CharField(max_length=20, blank=False)
	modelo_ascensor=models.CharField(max_length=20, blank=False)
	fallas_detectadas=models.CharField(max_length=200, blank=False)
	reparaciones=models.CharField(max_length=200, blank=False)
	piezas_cambiadas=models.CharField(max_length=200, blank=True)
	tecnico=models.OneToOneField(Usuario,null=False,blank=False,on_delete=models.CASCADE)
	cliente=models.OneToOneField(Cliente, null=False,blank=False,on_delete=models.CASCADE)


	def __str__(self):
		return self.nro_folio
		
