from django.contrib import admin
from solicitudes.models import Solicitudes
from django_object_actions import DjangoObjectActions
#from solicitudes.reports import Solicitudes
#from django.contrib.auth.models import User


# class ArticleAdmin(DjangoObjectActions, admin.ModelAdmin):
# 	def publish_this(self, request, obj):
# 		publish_obj(obj)
# 	publish_this.label = "Publish"	#opcional
# 	publish_this.short_description = "Publicar este articulo"

# 	objectations = ('publish_this')

class SolicitudesAdmin(admin.ModelAdmin):
	fieldsets = [
		('Datos Basicos', {'fields': ['nombre', 'snombre', 'apellido', 'sapellido', 'cedula', 'telefono1', 'telefono2', 'email', 'observaciones']}),
		('Datos Terreno', {'fields': ['terreno', 'tenencia'], 'classes': ['collapse']}),
		('Datos de Solicitud', {'fields': ['estado', 'municipio', 'parroquia', 'sector', 'calle', 'casa', 'ncasa'], 'classes': ['collapse']}),
		('Por el Ente', {'fields': ['ente']}),
	]
	list_display = ('nombre', 'apellido', 'cedula', 'telefono1', 'ente', 'estado', 'municipio', 'fecha_solicitud')
	list_filter = ['ente', 'fecha_solicitud']
	search_fields = ['cedula', 'nombre', 'apellido']
	actions = ['make_published']

	def make_published(self, request, queryset):
		queryset.update(status='p')
	make_published.short_description = "Marcar las solicitudes como publicadas"

admin.site.register(Solicitudes, SolicitudesAdmin)