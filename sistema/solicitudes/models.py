from django.db import models
from venezuela.models import Estado, Municipio, Parroquia
from smart_selects.db_fields import ChainedForeignKey
from django.contrib.auth.models import User


class Terreno(models.Model):
    terreno = models.CharField(max_length=2)

    def __unicode__(self):
    	return self.terreno

	class Meta:
		verbose_name = u'Posee'


class Propio(models.Model):
	terreno = models.ForeignKey('Terreno')
	propio = models.CharField(max_length=2)

	def __unicode__(self):
		return self.propio

	class Meta:
		verbose_name = u'Propio'


# class Servicio(models.Model):
# 	terreno = models.ForeignKey('Terreno')
#         propio = models.ForeignKey('Propio')
# 	servicio = models.CharField(max_length=2)

# 	def __unicode__(self):
# 		return self.servicio

# 	class Meta:
# 		verbose_name = u'Servicio'


# class Conyuge(models.Model):
# 	pareja = models.CharField(max_length=2, verbose_name="Tiene")
# 	nombre = models.CharField(max_length=20, verbose_name="Nombre")
# 	apellido = models.CharField(max_length=20, verbose_name="Apellido")
# 	cedula = models.CharField(
# 		max_length=8, 
# 		unique=True,
# 		error_messages={'unique': "La pareja tiene una solicitud en el sistema"}
# 		)


class Solicitudes(models.Model):
	nombre = models.CharField(max_length=12)
	snombre = models.CharField(max_length=12, null=True, blank=True, verbose_name="Segundo Nombre")
	apellido = models.CharField(max_length=15)
	sapellido = models.CharField(max_length=15, null=True, blank=True, verbose_name="Segundo Apellido")
	cedula = models.CharField(max_length=8, unique=True, error_messages={'unique': "Ya existe una solicitud con esta Cedula"})
	nacimiento = models.DateField(null=True, blank=True)
	telefono1 = models.CharField(max_length=11, verbose_name="Telf. Celular")
	telefono2 = models.CharField(max_length=11, blank=True, verbose_name="Telf. Fijo")
	email = models.EmailField(max_length=32, verbose_name="Correo Electronico")
	observaciones = models.TextField(error_messages={'blank': "Escriba una observacion"})
	# pareja = models.ForeignKey(Conyuge.pareja)
	# pnombre = models.ForeignKey(Conyuge.nombre)
	# papellido = models.CharField(max_length=20, verbose_name="Apellido de pareja")
	# pcedula = models.CharField(
	# 	db_column="cedula",
	# 	max_length=8,
	# 	unique=True,
	# 	error_messages={'unique': "La pareja tiene una solicitud en el sistema"},
	# 	verbose_name="Cedula"
	# 	)
	terreno = models.ForeignKey(Terreno, verbose_name="Posee")
    	tenencia = ChainedForeignKey(
            Propio,
            chained_field="terreno",
            chained_model_field="terreno",
            show_all=False,
            auto_choose=True,
            verbose_name="Propio"
            )
	# servicios = ChainedForeignKey(
 #            Servicio,
 #            chained_field="propio",
 #            chained_model_field="propio",
 #            show_all=False,
 #            auto_choose=True
 #            )
	estado = models.ForeignKey(Estado)
	municipio = ChainedForeignKey(
            Municipio,
            chained_field="estado",
            chained_model_field="estado",
            show_all=False,
            auto_choose=True
            )
	parroquia = ChainedForeignKey(
            Parroquia,
            chained_field="municipio",
            chained_model_field="municipio",
            show_all=False,
            auto_choose=True
            )
	sector = models.CharField(max_length=150)
	calle = models.CharField(max_length=20, verbose_name="Av./Calle")
	casa = models.CharField(max_length=20, verbose_name="Edificio/Casa", null=True)
	ncasa = models.CharField(max_length=4, verbose_name="N Casa/Apartamento", null=True)
	ente = models.ForeignKey(User, related_name='entries')
	fecha_solicitud = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Solicitud")


def __unicode__(self):
    return self.name

class Admin:
    pass