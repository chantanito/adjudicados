from django.contrib import admin
# Register your models here.
from adjudicados.models import Adjudicado, DatosSociales, Terreno
#from adjudicados.forms import Terreno

class DatosSocialesEnLinea(admin.TabularInline):
	model = DatosSociales
	extra = 0
	#code

class TerrenoAdmin(admin.ModelAdmin):
	pass
#	model = Terreno
#	extra = 0
#	fieldsets = [
#		('Datos de Terreno', {'fields': ['posesion', 'titularidad', 'servicios']})
#	]

class AdjudicadoAdmin(admin.ModelAdmin):
	pass
#	fieldsets = [
#	('Datos Basicos',{'fields': ['nombre', 'apellido', 'cedula', 'segundo_nombre', 'segundo_apellido']}),
#	('Datos Adicionales',{'fields': ['telefono_1', 'direccion', 'correo_electronico', 'fecha_de_nacimiento', 'telefono_2'], 'classes': ['collapse']})
#	]
#	inlines = [DatosSocialesEnLinea]
	#inlines = [TerrenoAdmin]
#	list_display = ('nombre', 'apellido', 'cedula', 'fecha_de_publicacion')
#	list_filter = ['fecha_de_publicacion']
#	search_fields = ['cedula', 'nombre']

admin.site.register(Adjudicado, AdjudicadoAdmin)
admin.site.register(Terreno, TerrenoAdmin)