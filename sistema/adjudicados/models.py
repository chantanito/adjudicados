import datetime
from django.db import models
from django.utils import timezone
#from smart_selects.db_fields import ChainedForeignKey
# from django import forms

# Create your models here.
class Adjudicado(models.Model):
    nombre = models.CharField(max_length=10)
    segundo_nombre = models.CharField(max_length=10, null=True, blank=True)
    apellido = models.CharField(max_length=10)
    segundo_apellido = models.CharField(max_length=10, null=True, blank=True)
    cedula = models.CharField(max_length=8, unique=True)
    fecha_de_nacimiento = models.DateTimeField(null=True, blank=True)
    correo_electronico = models.EmailField(null=True, blank =True)
    direccion = models.CharField(max_length=300)
    telefono_1 = models.CharField(max_length=11)
    telefono_2 = models.CharField(max_length=11, null=True, blank=True)
    fecha_de_publicacion = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.nombre + " " + self.apellido + " - " + self.cedula + " - " + self.telefono_1

    class Admin:
        pass

class Terreno(models.Model):
    OPCIONES_TERRENO = (
        ('S', 'Si'),
        ('N', 'No'),
        )
    terreno = models.ForeignKey(Adjudicado)
    posesion = models.CharField(max_length=2, choices=OPCIONES_TERRENO)
    titularidad = models.CharField(max_length=2, choices=OPCIONES_TERRENO)
    servicios = models.CharField(max_length=2, choices=OPCIONES_TERRENO)

    def __unicode__(self):
        return self.posesion + "" + self.titularidad + " - " + self.servicios

    class Admin:
        pass

class DatosSociales(models.Model):
    pareja = models.ForeignKey(Adjudicado)
    pnombre = models.CharField(max_length=10)
    psegundo_nombre = models.CharField(max_length=10, null=True, blank=True)
    papellido = models.CharField(max_length=10)
    psegundo_apellido = models.CharField(max_length=10, null=True, blank=True)
    pcedula = models.CharField(max_length=8, unique=True)
    
    def __unicode__(self):
        return self.pnombre

class InscritosPsuv(models.Model):
    psuv = models.ForeignKey(Adjudicado)
    cedula = models.CharField(max_length=8)
    nombre = models.CharField(max_length=40)
    primer_apellido = models.CharField(max_length=25)
    tel1 = models.CharField(max_length=11)
    tel2 = models.CharField(max_length=11, null=True, blank=True)
    tel3 = models.CharField(max_length=11, null=True, blank=True)
    segundo_nombre = models.CharField(max_length=25, null=True, blank=True)
    segundo_apellido = models.CharField(max_length=25, null=True, blank=True)
    nacionalidad = models.CharField(max_length=2)
    municipio = models.CharField(max_length=20)
    parroquia = models.CharField(max_length=20)




    def __unicodes__(self):
        return self.nombre