from django.db import models

class Solicitante(models.Model):
	nombre = models.CharField(max_length=12,blank,)
	snombre = models.CharField(max_length=12
