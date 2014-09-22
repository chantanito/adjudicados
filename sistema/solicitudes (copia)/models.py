from django.db import models

class Solicitudes(models.Model):
	nombre = models.CharField(max_length=12)
	snombre = models.CharField(max_length=12, null=True, blank=True)
	apellido = models.CharField(max_length=15)
	sapellido = models.CharField(max_length=15, null=True, blank=True)
	cedula = models.CharField(max_length=8, unique=True)
	nacimiento = models.DateField(null=True, blank=True)
	telefono1 = models.CharField(max_length=11)
	telefono2 = models.CharField(max_length=11, blank=True)
	email = models.EmailField()
	observaciones = models.TextField()

	def __unicode__(self):
	  	return self.name

	class Admin:
		pass